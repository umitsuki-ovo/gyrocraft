import psutil

# 現在実行されているすべてのプロセスを取得
processes = list(psutil.process_iter())

# 実行中のすべてのプロセスについてループ
for process in processes:
    try:
        # プロセスの名前、プロセスID、メモリ使用量、およびCPU使用量を出力
        process_name = process.name()
        process_id = process.pid
        cmdline = process.cmdline()
        cpu_percent = process.cpu_percent()
        print(f"Name: {process_name}, PID: {process_id}, Memory Usage: {cmdline}, CPU Usage: {cpu_percent}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # プロセスがすでに終了している、アクセスが拒否されている、またはZombieプロセスの場合、処理を続行する
        continue

"""memo
pid = subprocess.Popen('pidof bedrock_server', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
subprocess.Popen(f'kill -9 {pid}', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

"""
