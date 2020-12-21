import asyncio
import os
from enum import Enum

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

    def write_handler(self, message, writer):
        """Method for concurrent message write"""
        self.tasks.add(asyncio.create_task(write_util(writer, message)))

    async def handle_request(self, reader, writer):
        """Method to handle request"""
        self.write_handler(b"Who are you? provide username|password\n", writer)

        async for data in read_util(reader):  # ended when we close the connection of client
            print("Received:", data.decode())
            self.write_handler(data, writer)

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
