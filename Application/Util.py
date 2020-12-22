from asyncio import StreamWriter, StreamReader, Queue
from typing import AsyncIterator


async def write_util(writer: StreamWriter, message: bytes):
    """write utility class"""
    if not message.endswith(b"\n"):
        message += b"\n"

    writer.write(message)
    print("Sending:", message.decode())
    await writer.drain()


async def read_util(reader: StreamReader) -> AsyncIterator[bytes]:
    """read utility class, make sure all data comes with new line appended"""
    data = b""
    try:
        while data := await reader.read(100):
            if b"\n" in data:
                message, data = data.split(b"\n", 1)
                yield message

    except ConnectionResetError:
        pass
    if data:
        yield data


async def write_from_queue(writer: StreamWriter, queue: Queue):
    """Function to write message from queue"""
    try:
        while (message := await queue.get()) != b"":
            await write_util(writer, message)
    finally:
        await writer.drain()
        writer.close()
