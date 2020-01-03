#!/usr/bin/python3
import requests, sys, os
from codes import Constants, SimpleParser, ParseAi, Autocomplete
from codes.Constants import bash
from colorama import Fore, Style
import subprocess, readline, threading
import socketio, asyncio, os

kivia = SimpleParser.KiviaLogic()

sio = socketio.AsyncClient()
loop = asyncio.get_event_loop()

Constants.COLOR_TERMINAL = Fore.GREEN


def colored(color, s):
    return Style.BRIGHT + color + s + Style.RESET_ALL


def fetchSystemMessage():
    kivia.db.delete('sys_messages', {'seen': 1})
    messages = kivia.db.get('sys_messages', {'seen': 0})
    if messages:
        print(messages[0][0])
        kivia.db.conn.execute("update sys_messages set seen=1 where t='" + messages[0][1] + "'")
        kivia.db.conn.commit()


def first():
    try:
        sys.stdout.write("\x1b]2;" + "(" + bash("whoami") + ") [ " + os.getcwd() + " ] \x07")
        fetchSystemMessage()
        cmd = input(colored(Constants.COLOR_TERMINAL, " -> "))
        if cmd == "exit":
            sys.exit(0)
        elif "cd" in cmd:
            path = cmd.replace("cd ", "")
            try:
                os.chdir(os.path.expanduser(path))
            except Exception as e:
                print(str(e))
        else:
            try:
                if [x for x in kivia.getCommands() if str(cmd).startswith(x)]:
                    raise Exception("Got it")
                Constants.COLOR_TERMINAL = Fore.GREEN
                count = len([x for x in cmd if x == "'"])
                cmd = cmd if count % 2 == 0 else cmd.replace("'", "")
                req = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
                out, err = req.communicate()
                if str(err) != "b''":
                    err = str(err).replace("b'", "'").replace('b"', '"')
                    if ": not found" not in err:
                        os.system("echo " + err)
                    else:
                        raise Exception("command not found")
            except:
                if cmd != "":
                    if kivia.check(cmd) is False:
                        try:
                            if ParseAi.parse(requests.get(Constants.URL + cmd).json()) is False:
                                Constants.COLOR_TERMINAL = Fore.RED
                                print(colored(Fore.RED, "Kivia : Command  not found !"))
                        except:
                            Constants.COLOR_TERMINAL = Fore.RED
                            print(colored(Fore.RED, "Kivia : Command not found !"))
        first()
    except KeyboardInterrupt:
        print("\r")
        first()


@sio.on('connect')
async def on_connect():
    await sio.emit('join',
                   {"password": "wisdomrider",
                    "uid": os.popen("cat /sys/class/net/enp1s0/address").read()[:-1]})


@sio.on("server")
def serverresponse(msg):
    db = SimpleParser.DB()
    db.conn.execute("INSERT INTO sys_messages (`message`) VALUES ('" + msg + "');")
    db.conn.commit()


async def start():
    try:
        await sio.connect('http://localhost:3000')
        await  sio.wait()
    except:
        pass


def startSocket():
    loop.run_until_complete(start())


socketthread = threading.Thread(target=startSocket)
socketthread.start()
first()
