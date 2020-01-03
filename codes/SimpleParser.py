from codes.Database import *
from codes.Constants import *
import random, re, os


class KiviaLogic:
    user_commands = ["add command ", "update command ", "delete command "]

    def getCommands(self):
        blockedCommands = self.db.getAll('blocked_commands')
        userCommands = self.db.getAll('user_commands')
        blockedCommands = [x[0] for x in blockedCommands]
        userCommands = [x[0] for x in userCommands]
        return blockedCommands + userCommands

    def __init__(self):
        self.db = DB()
        self.lastintent = ""

    def check(self, userinput: str):
        if userinput == "adminpanel":
            import codes.adminpanel
            codes.adminpanel.input1()
            return True
        reply = None
        try:
            user_command = self.db.get('user_commands', {"cmd": userinput})
        except:
            return False

        # Checking for user commands or add/update/delete command

        if user_command:
            os.system(self.parseEmojis(user_command[0][1]))
            return True
        elif self.user_commands[0] in userinput:
            return self.customCommand(userinput.replace(self.user_commands[0], ""), 0)
        elif self.user_commands[1] in userinput:
            return self.customCommand(userinput.replace(self.user_commands[1], ""), 1)
        elif self.user_commands[2] in userinput:
            return self.customCommand(userinput.replace(self.user_commands[2], ""), 2)
        else:

            # Searching for Intents and saving in db

            for x in self.db.getAll('intent_vars'):
                var = str(x[1])
                intent = str(x[0])
                commandtype = str(x[2])
                var_ = []
                for x in re.findall("{.*?}", var):
                    var_.append(str(x).replace("{", "").replace("}", ""))
                    var = var.replace(x, "(.*)")
                    r = re.compile(var).search(userinput)
                    if r is not None:
                        self.db.updateIntent(var_[0], r.group(1), commandtype)
                        print(colored(self.checkformessages(intent)))
                        return True

                #  Searching for Commands and fetching replies

                for x in self.db.getAll('intent_cmds'):
                    if reply is not None:
                        break
                    intentname = str(x[0])
                    pattern = str(x[1]).strip()
                    pattern = pattern[:-2] if pattern.endswith(";;") else pattern
                    startsfrom = str(x[2])
                    lastintent = str(x[3])
                    if lastintent == "" or lastintent == self.lastintent:
                        if startsfrom == "B":
                            for y in pattern.split(";;"):
                                if userinput.lower().startswith(str(y)):
                                    reply = self.checkformessages(intentname)
                                    break
                        elif startsfrom == "E":
                            for y in pattern.split(";;"):
                                if userinput.lower().endswith(str(y)):
                                    reply = self.checkformessages(intentname)
                                    break
                        elif startsfrom == "BE":
                            for y in pattern.split(";;"):
                                if userinput.lower().endswith(str(y)) or userinput.lower().startswith(str(y)):
                                    reply = self.checkformessages(intentname)
                                    break
                        elif startsfrom == "C":
                            for y in pattern.split(";;"):
                                if str(y) in userinput:
                                    reply = self.checkformessages(intentname)
                                    break
        if reply is None:
            return False
        else:
            print(colored(reply))
            return True

    def customCommand(self, cmd, i):
        if i is 0 or i is 1:
            print(colored("Enter Bash Command To Save in " + cmd + " ", emoji=HAPPY))
            x = input(colored("(" + cmd + ") : ", center=0))
        if i is 0:
            try:
                self.db.insert('user_commands', (cmd, x))
                print(colored("Command added Successfully ! ", emoji=HAPPY))
            except:
                print(colored("Command already exists.Please update it or remove it ", emoji=SAD))
        elif i is 1:
            self.db.update('user_commands', (cmd, x), where={'cmd': cmd})
            print(colored("Command updated Successfully ! ", emoji=HAPPY))
        else:
            self.db.delete('user_commands', {'cmd': cmd})
            print(colored("Command deleted Successfully ! ", emoji=HAPPY))
        return True

    def checkformessages(self, x):
        self.lastintent = x
        msgs = self.db.get('intent_msgs', {'intent': x})

        # Randomizing the message

        msg = msgs[random.randrange(len(msgs))]

        # Parsing Variables

        reply = str(msg[1])
        reply = self.parseEmojis(reply)
        values = re.findall("#[aA-zZ]*", reply)

        for x in values:
            parsed = self.db.get('parser', {'parse': str(x).replace("#", "").strip()})
            bashresult = bash(parsed[0][1]) if parsed[0][2] is not "E" else bash("echo " + parsed[0][1])
            reply = reply.replace(x, bashresult + '')

        # Finding Hidden Commands to Execute

        cmds = re.findall("{.*?}", reply)
        for x in cmds:
            bash(str(x).replace("{", "").replace("}", ""))
            reply = reply.replace(x, "")

        # After parsing returning the value
        return reply

    def parseEmojis(self, text: str):
        if "#EMOJIH" in text:
            text = text.replace("#EMOJIH", Emojis.getHappyEmoji())
        elif "#EMOJIS" in text:
            text = text.replace("#EMOJIS", Emojis.getSadEmoji())
        elif "#EMOJIA" in text:
            text = text.replace("#EMOJIA", Emojis.getAnimalEmoji())
        elif "#EMOJIN" in text:
            text = text.replace("#EMOJIN", Emojis.getNatureEmoji())
        elif "#EMOJIT" in text:
            text = text.replace("#EMOJIN", Emojis.getTravelEmoji())
        return text
