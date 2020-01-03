import readline, glob, os

from codes.Constants import bash


def autoComplete(tab):
    import subprocess
    process = subprocess.run(f"compgen -c {tab}", executable="/bin/bash", shell=True, stdout=subprocess.PIPE)
    return [x for x in process.stdout.decode("utf-8").split("\n") if x != ""][:5]


def completer(text, state):
    return (autoComplete(text) + [None])[state]
    # return ""
    # isCd = str(text).startswith("cd")
    # options = (glob.glob(text + '*') + [None])[state]
    # if len(text) > 1 and not isCd:
    #     options1 = (glob.glob1("/bin/", text + "*") + [None])[state]
    #     systemCmds = (glob.glob1("/sbin/", text + "*") + [None])[state]
    # elif text == "":
    #     x = [b for b in os.listdir(os.curdir) if not str(b).startswith(".")]
    #     return x[state]
    # if options is not None:
    #     return None if not os.path.isdir(options) else options
    # elif options is None and options1 is not None:
    #     return options1
    # elif options1 is None and systemCmds is not None:
    #     return systemCmds
    # elif systemCmds is None:
    #     pass


readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab:complete")
readline.set_completer(completer)
