from codes.Constants import *
from codes.Database import *


def input1():
    os.system("clear")
    os.system("figlet Admin Panel|lolcat")
    print(colored(
        "\n 1.add a intent_cmd\n 2.add a intent_msg"
        "\n 3.add a intent_var\n 4.add a parser\n 5.add a blocked command"
        "\n 6.delete a intent_cmd \n 7.update a intent_cmd"
        "\n 8.delete a intent_msg \n 9.update a intent_msg")
    )
    x = int(input(colored("-->", center=0)))
    db = DB()
    try:
        if x == 1:
            intent = input(colored("\nEnter intent : ", center=0))
            cmd = input(colored("\nEnter Cmd : ", center=0))
            frm = input(colored("\nFrom where : ", center=0))
            last_intent = input(colored("\nAny last intent : ", center=0))
            db.insert('intent_cmds', (intent, cmd, frm, last_intent))
            print(colored("Intent Added successfully. " + Emojis.getNatureEmoji()))
        elif x == 2:
            intent = input(colored("\nEnter intent : ", center=0))
            msg = input(colored("\nEnter message : ", center=0))
            db.insert('intent_msgs', (intent, msg))
            print(colored("Intent message added successfully. " + Emojis.getNatureEmoji()))
        elif x == 3:
            intent = input(colored("\nEnter intent : ", center=0))
            pattern = input(colored("\nEnter Pattern : ", center=0))
            var_type = input(colored("\nWhat type of command : ", center=0))
            db.insert('intent_vars', (intent, pattern, var_type))
            print(colored("Intent var added successfully. " + Emojis.getNatureEmoji()))
        elif x == 4:
            parse = input(colored("\nEnter parse : ", center=0))
            msg = input(colored("\nEnter message : ", center=0))
            typee = input(colored("\nWhat type of command : ", center=0))
            db.insert('parser', (parse, msg, typee))
            print(colored("Parser added successfully. " + Emojis.getNatureEmoji()))
        elif x == 5:
            cmd = input(colored("\nEnter command to block : ", center=0))
            db.insert('blocked_commands', (cmd,))
            print(colored("Command added to blocked list " + Emojis.getHappyEmoji()))
        elif x == 6:
            pass
        elif x == 7:
            pass
        elif x == 8:
            pass
        else:
            pass
    except:
        print(colored("Something went wrong please retry.", emoji=SAD))
