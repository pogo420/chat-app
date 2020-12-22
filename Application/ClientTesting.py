import asyncio
import contextlib
import os
import sys
from asyncio import Queue

from Util import write_util, read_util, write_from_queue
import aiofiles.threadpool as nbt


async def read_handler(reader):
    """Read handler for concurrent read"""
    async for data in read_util(reader):
        print(f'Received: {data.decode()!r}')


async def stream_to_queue(file, write_queue):
    """Function to save streams to queue"""
    loop = asyncio.get_event_loop()
    async for message in nbt.wrap(file, loop=loop):  # non blocking io read
        await write_queue.put(message.encode())


async def main(file):
    reader, writer = await asyncio.open_connection(
        os.environ["SERVER_HOST"],
        os.environ["SERVER_PORT"])

    write_queue = Queue()
    rh = asyncio.create_task(read_handler(reader))  # concurrent reading
    wh = asyncio.create_task(write_from_queue(writer, write_queue))  # concurrent write from queue
    ch = asyncio.create_task(stream_to_queue(file, write_queue))  # concurrent stdin to queue

    done, pending = await asyncio.wait([rh,
                                        wh,
                                        ch],
                                       return_when=asyncio.FIRST_COMPLETED)

    print("Closing connection")  # reaches when we cancel the connection
    for task in pending:  # closing the pending connections
        task.cancel()


if __name__ == "__main__":
    asyncio.run(main(sys.stdin))  # check why stdin works not input, does not strip new line
