import subprocess
import datetime
import shutil
import os

def server_kill(process_name):
    pid = subprocess.getoutput(f'pidof {process_name}')
    subprocess.Popen(f'kill -9 {pid}', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    backup_log(pid)

def backup_log(terminal):
    logfile = './temp/backuplog'
    now = datetime.datetime.now()
    text = f"{now}:   {terminal}killed.\n"

    with open(logfile, "a") as file:
        file.write(text)

def backup():
    server_kill('bedrock_server')
    now_time = datetime.datetime.now()
    shutil.copytree('./bedrock_server/', f'./temp/{now_time.month}/{now_time}', dirs_exist_ok = True)
    if os.path.isdir(f'./temp/{now_time.month + 7}') == True:
        shutil.rmtree(f'./temp/{now_time.month + 7}')

backup()
