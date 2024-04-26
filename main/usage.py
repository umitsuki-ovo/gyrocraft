import time
import psutil
import schedule
import speedtest
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "bucket"
org = "org"
token = 'token'
url="http://localhost:8086"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)
client = client.write_api(write_options=SYNCHRONOUS)

def db_write(date_name, num):
    pp = (
        Point(date_name)
        .tag("location", "gyrocraft_server1")
        .field(num)
    )
    client.write(bucket=bucket, org=org, record=pp)

def get_info():
    cpu_info = psutil.cpu_percent(percpu=True)
    memory_info = psutil.virtual_memory().percent

    st = speedtest.Speedtest()
    st.get_best_server()

    download_result = st.download()
    upload_result = st.upload()
    ping = st.results.ping

    db_write("CPU", cpu_info)
    db_write("Memory", memory_info)
    db_write("Download", download_result)
    db_write("Upload", upload_result)
    db_write("ping", ping)


schedule.every(1).minutes.do(get_info)
while True:
    schedule.run_pending()
    time.sleep(1)