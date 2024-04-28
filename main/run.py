import subprocess
import schedule
import time

def main():
    subprocess.Popen("python3 main.py", shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

if __name__ == '__main__':
    subprocess.Popen("python3 main.py", shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

schedule.every().wednesday.at('12:00').do(main)
while True:
    schedule.run_pending()
    time.sleep(1) 