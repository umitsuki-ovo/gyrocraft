import subprocess
import datetime


def start_minecraft():
    r = subprocess.Popen('LD_RIBRARY_PATH=. ./bedrock_server', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    for line in iter(r.stdout.readline,b''):
        terminal_log(line.rstrip().decode("utf8"))

def terminal_log(terminal):
    logfile = '../temp/terminallog'
    now = datetime.datetime.now()
    text = f"{now}:   {terminal}\n"

    with open(logfile, "a") as file:
        file.write(text)

start_minecraft()
