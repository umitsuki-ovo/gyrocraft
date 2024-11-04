import subprocess
import datetime
import shutil
import os

def server_kill(process_name):
    pid = subprocess.getoutput(f'pidof {process_name}')
    subprocess.Popen(f'kill -9 {pid}', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    if '/home/gyrocraft_bedrock/..' != dir:
        os.chdir(dir)
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
    shutil.copytree('./bedrock_server/', f'./temp/data/{now_time.month}/{now_time}', dirs_exist_ok = True)
    delmonth = now_time.month + 7
    if delmonth > 12:
        delmonth -= 12
    if os.path.isdir(f'./temp/data/{delmonth}') == True:
        shutil.rmtree(f'./temp/data/{delmonth}')

backup()
