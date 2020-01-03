from colorama import Fore, Style
import random, os, codes.Emojis as Emojis

COLOR_TERMINAL = ""
CMDS = "CMDS"
CMDPARSER = "cmdparser"
URL = "http://localhost:2847/parse?q="
processes = ["install", "open", "reboot", "shutdown", "ls"]
colors = [Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.WHITE, Fore.GREEN, Fore.LIGHTRED_EX]

HAPPY = 0
SAD = 1
ANGRY = 2


def bash(s):
    return os.popen(s).read()[:-1]


EmoJi = {0: Emojis.getHappyEmoji, 1: Emojis.getSadEmoji, 2: Emojis.getSadEmoji,
         3: Emojis.getBlank, 4: Emojis.getAnimalEmoji}


def colored(s, **param):
    center = param['center'] if 'center' in param else 100
    emoji = param['emoji'] if 'emoji' in param else 3
    color = colors[random.randrange(len(colors))]
    return str(Style.BRIGHT + color + s + Style.RESET_ALL + " " + EmoJi.get(emoji)()).center(center)
