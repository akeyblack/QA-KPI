import asyncio
import socketio

import hashlib

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('Connection established')

@sio.event
async def trans(data):
    print(data['checksum'])
    hash = hashlib.md5(data['data'].encode('utf-8')).hexdigest()
    if hash == data['checksum']:
        print('Done succesfully')
        with open("../clientdata/data.txt", "w+") as file:
            file.write(data['data'])
            print('Written to file')


@sio.event
def disconnect():
    print('Disconnected ')


async def main():
    await sio.connect('http://server:5000')
    await sio.wait()

if __name__ == '__main__':
    asyncio.run(main())