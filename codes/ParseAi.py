from codes import Emojis
import os


def response(param):
    from codes.Constants import colored
    print(colored(param + " " + Emojis.getHappyEmoji()))


def parse(json):
    intent = json["intent"]["name"]
    entities = getEntities(json["entities"])

    if not entities:
        return False
    if intent == "open_url":
        url = getEntityValue(["URL"], entities)
        import webbrowser
        response("opening : https://" + url + ".com")
        webbrowser.open_new("https://" + url + ".com")
    elif intent == "sys_command":
        cmd = getEntityValue(["cmd"], entities)
        os.system(cmd + " now")
    elif intent == "install":
        cmd = getEntityValue(["package"], entities)
        os.system("sudo apt install " + cmd)
    elif intent == "install_on":
        module = getEntityValue(["module"], entities)
        package = getEntityValue(["package"], entities)
        os.system(package + " install " + module)
    else:
        return False
    return True


def getEntities(entities):
    entity = []
    for x in entities:
        entity.append({"entity": x["entity"], "value": x["value"]})
    return entity


def getEntityValue(param, entities):
    for x in entities:
        for y in param:
            if x["entity"] in y:
                return x["value"]
