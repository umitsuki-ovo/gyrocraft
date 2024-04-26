import subprocess
import datetime
import schedule
import psutil
import shutil
import time
import os

def server_kill(process_name):
    process_pid = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            process_pid = proc.info['pid']
            break
        print('Process not found.')
        break
    psutil.Process(process_pid).kill()

def start_minecraft():
    r = subprocess.popen('LD_RIBRARY_PATH=. ./bedrock_server', stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    for line in iter(r.stdout.readline,b''):
        terminal_log(line.rstrip().decode("utf8"))

def backup():
    server_kill('bedrock_server')
    now_time = datetime.datetime.now()
    shutil.copytree('bedrock/', f'temp/{now_time.month}/{now_time}', dirs_exist_ok = True)
    if os.path.isdir(f'temp/{now_time.month + 7}') == True:
        shutil.rmtree(f'temp/{now_time.month + 7}')

def terminal_log(terminal):
    logfile = 'temp/'
    now = datetime.datetime.now()
    text = f"{now}:   {terminal}\n"

    with open(logfile, "terminallog") as file:
        file.write(text)

def main():
    backup()
    start_minecraft()
   
start_minecraft()
if __name__ == "__main__":
    main()

schedule.every.wednesday.at('12:00').do(main)
while True:
    schedule.run_pending()
    time.sleep(1) 