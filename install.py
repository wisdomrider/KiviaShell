#!/usr/bin/python3
from codes.Constants import *
import os


def last():
    os.system("mv " + os.getcwd() + " /usr/local/etc/kivia")
    os.system('echo "exec python3 /usr/local/etc/kivia">>/etc/bash.bashrc')
    print(colored("Thanks !"))


def ask():
    cmd = input(colored("(Y/N) -> ", center=0))
    if str(cmd).lower() == "y":
        os.system("ai/install_ai.sh")
        os.system("clear")
        os.system("sudo cp kivia.service /lib/systemd/system")
        os.system("sudo systemctl start kivia")
        last()
        print(colored("Reboot your system to start working with kivia with AI"))
    elif str(cmd).lower() == "n":
        last()
        print(colored("Kivia is now located at /usr/local/etc"))
    else:
        print(colored("Please Say (Y) for yes or (N) for no"))
        ask()


os.system("clear")
print(colored("You are welcome to Kivia shell !", emoji=HAPPY))
print("\r")
print(colored("Would you like to install artificial intelligence to your shell?", emoji=HAPPY))
ask()
