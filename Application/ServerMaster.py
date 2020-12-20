import asyncio
import os
from enum import Enum

from MessageParser import MessageParser
from AuthenticationMaster import AuthenticationMaster


class Status(Enum):
    Authenticated="Authenticated"
    NotAuthenticated="NotAuthenticated"
    InvalidMessageFormat="InvalidMessageFormat"


class ServerMaster:
    """Class for Async Server Manager"""

    def __init__(self):
        self.host = os.environ["SERVER_HOST"]
        self.port = os.environ["SERVER_PORT"]
        self.chat_db = os.environ["CHAT_DB"]
        self.auth_manager = AuthenticationMaster(self.chat_db)
        self.users = {}

    async def server_parser(self, message, writer):
        """Method for parsing message"""
        mp = MessageParser()
        user = None
        to = None
        send_message = None
        login_message = mp.parse_login(message)
        print("Hello")

        if login_message is not None:
            user, passw = login_message
            # check for authenticated
            if self.auth_manager.is_authenticated(user) is False:
                self.auth_manager.authenticate(user, passw)
            if self.auth_manager.is_authenticated(user) is True:
                self.users[user] = writer
                return Status.Authenticated, None
            else:
                return Status.NotAuthenticated, None
        # if user is not logged
        # elif user is None:
        #     print("user is none", self.users)
        #     return Status.NotAuthenticated, None
        # extracting message
        elif mp.validate_message(message):
            to, send_message = mp.parse_message(message)
            self.users.get(to).write(send_message.encode("utf-8"))
            print(self.users)
            return Status.Authenticated, (to, send_message)
        else:
            print("invalid")
            return Status.InvalidMessageFormat, None
        return

    async def handle_request(self, reader, writer):
        """Method to handle request"""
        data = await reader.read(100)
        message = data.decode()
        # addr = writer.get_extra_info('peername')
        # print(f"Received {message!r} from {addr!r}")
        # print(f"Send: {message!r}")

        response, data = await self.server_parser(message, writer)

        if response == Status.Authenticated:
            if data is None:
                writer.write(response.value.encode("utf-8"))
            else:
                writer.write(str(data).encode("utf-8"))

        writer.write(response.value.encode("utf-8"))
        await writer.drain()

    async def start(self):
        """Method for starting server"""
        server = await asyncio.start_server(
            self.handle_request,  self.host, self.port)

        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(ServerMaster().start())

