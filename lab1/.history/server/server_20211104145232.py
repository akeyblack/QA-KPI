import sys

from aiohttp import web
import socketio

import secrets
import hashlib

app = web.Application()
sio = socketio.AsyncServer(async_mode="aiohttp")
sio.attach(app)

with open("../serverdata/data.txt", "w+") as file:
    data = secrets.token_hex(nbytes=1024)
    file.write(data)

@sio.event
async def connect(sid, environ):
    with open("../serverdata/data.txt", "r") as file:
        print("connect ", sid)
        data = file.read()
        hash = hashlib.md5(data.encode('utf-8')).hexdigest()
        await sio.emit("trans", (
            {"data": data, "checksum": hash}
            ), to=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == "__main__":
    if len(sys.argv)>1:
        try:
            p = int(sys.argv[1])
            web.run_app(app, port=p)
        except Exception:
            print ("Wrong port")