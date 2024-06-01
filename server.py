import re
import zipfile
import os
import requests
import shutil
import urllib.request
from requests.exceptions import Timeout
from backup import server_kill

version_text = "../temp/version.text"
extract_to_dir = "../temp/update/bedrock_server"
server_path = "./bedrock_server"
url = ""
filepath = ""

def get_content():
    try:
        response = requests.get("https://minecraft.net/en-us/download/server/bedrock/", timeout=30)
        content = response.text
        return content
    except Timeout:
        print("タイムアウトしました。")
        pass

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

def update(path):
    filepath = f"../temp/update/{path}"
    file_url = f"https://minecraft.azureedge.net/bin-linux/{path}"
    copy_path = f"../temp/update/"
    copy_file = "./bedrock_server/server.properties"
    urllib.request.urlretrieve(file_url, path)
    server_kill("bedrock_server")
    extract_zip(file_url)
    shutil.copy(copy_file, copy_path)
    shutil.copy(extract_to_dir, server_path)
    shutil.copy(f"{copy_path}/server.properties", server_path)


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