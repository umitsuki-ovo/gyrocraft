import subprocess
import schedule
import datetime
import time
import os

def main():
    subprocess.run("python3 ./update.py", shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    time.sleep(1)
    if today.weekday() == 2:
        backup()

def backup():
    subprocess.run("python3 ./backup.py", shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    time.sleep(1)
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bedrock_server'))
    subprocess.Popen('python3 main.py', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bedrock_server'))
    subprocess.Popen('python3 main.py', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

schedule.every().day.at("12:00").do(main)
while True:
    schedule.run_pending()
    time.sleep(1) 
