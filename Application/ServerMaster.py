import asyncio
import os
from asyncio import Queue
from enum import Enum
from typing import Dict

from Util import write_util, read_util, write_from_queue


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
        # self.queue = Queue()
        self.users: Dict['user', Queue] = {}

    async def handle_commands(self, reader, queue):
        """Method to process messages"""
        await queue.put(b"Who are you? provide username|password\n")

        logged_username = None  # temporary logged in user
        to = None  # temporary to user

        async for data in read_util(reader):  # ended when we close the connection of client
            print("Received:", data.decode())
            # self.write_handler(data, writer)
            text = data.decode()
            if text.startswith("$"):
                logged_username = text[1:]
                self.users[logged_username] = queue  # assigning the queue to the logged in user

            elif text.startswith("@"):
                if not logged_username:
                    await queue.put(b"Who are you? provide username|password\n")
                    continue
                to, message = text.split(" ", 1)
                to = to[1:]
                if to not in self.users:
                    await queue.put(b"Invalid username\n")

                user_message = f"{logged_username} {message}\n"
                await self.users.get(to).put(user_message.encode())  # putting message in respective queue of `to` user

    async def handle_request(self, reader, writer):
        """Method to handle request"""
        queue = Queue()
        wh = asyncio.create_task(write_from_queue(writer, queue))  # concurrent write
        await self.handle_commands(reader,queue)  # awaiting message process
        print("Closing connection")

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
