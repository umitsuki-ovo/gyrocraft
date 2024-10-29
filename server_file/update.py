import re
import zipfile
import os
import requests
import shutil
import urllib
import subprocess

version_text = "./temp/version.txt"
extract_to_dir = "./temp/update/bedrock_server"
server_path = "./bedrock_server"
url = ""
filepath = ""

def get_content():
    try:
        response = requests.get("https://minecraft.net/en-us/download/server/bedrock/", headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"}, verify=False, timeout=60)
        content = response.txt
        return content
    except Timeout:
        print("タイムアウトしました。")
        pass

def server_kill(process_name):
    pid = subprocess.getoutput(f'pidof {process_name}')
    subprocess.Popen(f'kill -9 {pid}', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

def check_version(version):
    with open(version_text, "r") as version_histry:
        last_version = version_histry.readlines()[-1].strip()
        if last_version == version:
            return 0
        else:
            return 1

def extract_zip(zip_file_path):
    if not os.path.exists(extract_to_dir):
        os.makedirs(extract_to_dir)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)

def copy(ext_dir,copy_dir)
    files = os.listdir(ext_dir)
    for file in files:
        ext_path = os.path.join(ext_dir, file)
        copy_path = os.path.join(copy_dir, file)
        if os.path.isfile(ext_path):
            shutil.copy(ext_path, copy_path)
        elif os.path.isdir(ext_path):
            shutil.copytree(ext_path, copy_path)

def update(url):
    version = url.split("/")[-1].split(".")[0]
    filepath = f"./temp/update/{version}"
    copy_path = f"./temp/update/"
    copy_file = "./bedrock_server/server.properties"
    copy_file2 = "./bedrock_server/main.py"
    urllib.request.urlretrieve(url, filepath)
    server_kill("bedrock_server")
    extract_zip(filepath)
    shutil.copy(copy_file, copy_path)
    shutil.copy(copy_file2, copy_path)
    copy(extract_to_dir, server_path)
    shutil.copy(f"{copy_path}/server.properties", server_path)
    shutil.copy(f"{copy_path}/main.py", server_path)


html = get_content()
if html is not None:
    match = re.search(r'<a href="(.*\.zip).*?">', html)
    if match:
        url = match.group(1)
        print(url)
    else:
        print("ZIPファイルのリンクが見つかりませんでした。")
else:
    print("アップデートに失敗しました。")

do_update = check_version(url)
if do_update == 1:
    update(url)
    with open(version_text, "a") as version_histry:
        version_histry.write(url + "\n")
        print("アップデートが完了しました。")
