import asyncio
import os


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        os.environ["SERVER_HOST"],
        os.environ["SERVER_PORT"])

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')


async def main():
    print("Introduce yourself: username|password")
    while True:
        await tcp_echo_client(input())


if __name__ == "__main__":
    asyncio.run(main())
