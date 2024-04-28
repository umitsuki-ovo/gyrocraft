import datetime
import psutil
import shutil
import os

def server_kill(process_name):
    logfile = '../temp/backuplog'
    now = datetime.datetime.now()
    process_pid = None
    for proc in psutil.process_iter(['pid', 'cmdline']):
        if proc.info['cmdline'] == process_name:
            process_pid = proc.info['pid']
            backup_log(process_pid)
            break
        backup_log('Process not found.')
        break
    psutil.Process(process_pid).kill()

def backup_log(terminal):
    logfile = '../temp/backuplog'
    now = datetime.datetime.now()
    text = f"{now}:   {terminal}\n"

    with open(logfile, "a") as file:
        file.write(text)

def backup():
    server_kill('/bin/sh -c LD_RIBRARY_PATH=. ./bedrock_server')
    server_kill('./bedrock_server')
    now_time = datetime.datetime.now()
    shutil.copytree('./', f'../temp/{now_time.month}/{now_time}', dirs_exist_ok = True)
    if os.path.isdir(f'../temp/{now_time.month + 7}') == True:
        shutil.rmtree(f'../temp/{now_time.month + 7}')

backup()
