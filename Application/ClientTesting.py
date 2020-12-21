import asyncio
import os
import sys
from Util import write_util, read_util
import aiofiles.threadpool as nbt


async def read_handler(reader):
    """Read handler for concurrent read"""
    async for data in read_util(reader):
        print(f'Received: {data.decode()!r}')


async def main(file):
    reader, writer = await asyncio.open_connection(
        os.environ["SERVER_HOST"],
        os.environ["SERVER_PORT"])

    rf = asyncio.create_task(read_handler(reader))  # concurrent execution
    loop = asyncio.get_event_loop()
    async for message in nbt.wrap(file, loop=loop):  # non blocking io read
        await write_util(writer, message.encode())
    rf.cancel()  # may be redundant
    await rf  # may be redundant


if __name__ == "__main__":
    asyncio.run(main(sys.stdin))  # check why stdin works not input
