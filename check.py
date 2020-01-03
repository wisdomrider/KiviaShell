import socketio, asyncio, os

import threading

sio = socketio.AsyncClient()

loop = asyncio.get_event_loop()


@sio.on('connect')
async def on_connect():
    await sio.emit('join',
                   {"password": "wisdomrideravi",
                    "uid": os.popen("cat /sys/class/net/enp1s0/address").read()[:-1]})
    print('I\'m connected!')
    await  sio.emit('broadcast', 'jp;a')


@sio.on('disconnect')
def on_disconnect():
    print('I\'m disconnected!')


@sio.on("server")
def serverresponse(msg):
    print(msg)


async def start():
    await sio.connect('http://localhost:3000')
    await  sio.wait()


def run():
    loop.run_until_complete(start())


def tyhreading():
    thread = threading.Thread(target=run)
    thread.start()


