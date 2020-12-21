import asyncio
import os
from enum import Enum
from typing import Dict

from Util import write_util, read_util


class Status(Enum):
    """Enums for status"""
    Authenticated = "Authenticated"
    NotAuthenticated = "NotAuthenticated"
    InvalidMessageFormat = "InvalidMessageFormat"


class ServerMaster:
    """Class for Async Server Manager"""

    def __init__(self):
        self.host = os.environ["SERVER_HOST"]
        self.port = os.environ["SERVER_PORT"]
        self.chat_db = os.environ["CHAT_DB"]
        self.tasks = set()
        self.users: Dict['user', 'writer'] = {}

    def write_handler(self, message, writer):
        """Method for concurrent message write"""
        self.tasks.add(asyncio.create_task(write_util(writer, message)))

    async def handle_request(self, reader, writer):
        """Method to handle request"""
        self.write_handler(b"Who are you? provide username|password\n", writer)
        logged_username = None  # temporary logged in user
        to = None  # temporary to user

        async for data in read_util(reader):  # ended when we close the connection of client
            print("Received:", data.decode())
            # self.write_handler(data, writer)
            text = data.decode()
            if text.startswith("$"):
                logged_username = text[1:]
                self.users[logged_username] = writer

            elif text.startswith("@"):
                if not logged_username:
                    self.write_handler(b"Who are you? provide username|password\n", writer)
                    continue
                to, message = text.split(" ", 1)
                to = to[1:]
                if to not in self.users:
                    self.write_handler(b"Invalid username\n", writer)
                user_message = f"{logged_username} {message}\n"
                self.write_handler(user_message.encode(), self.users.get(to))
                # self.users.get(username)(user_message.encode(), writer)

        print("Closing the connection")
        await asyncio.wait(self.tasks)

    async def start(self):
        """Method for starting server"""
        server = await asyncio.start_server(
            self.handle_request, self.host, self.port)

        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(ServerMaster().start())
