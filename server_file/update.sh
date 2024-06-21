#====================================================================
# kill server
#====================================================================

pid_server = $(pidof bedrock_server)
kill -9 $pid_server


#====================================================================
# update server
#====================================================================

cp -f ./bedrock_server/server.properties ../temp/update/
url = $(sed -n 's/.*href="\([^"]*\.zip\)".*/\1/p' https://minecraft.net/en-us/download/server/bedrock/ | grep -E '^https://minecraft.azureedge.net/bin-linux/.*\.zip$')
wget $url -O ../temp/update/bedrock_server
verson = $(basename "$url")
unzip $version
cp -f ../temp/update/bedrock_server ./bedrock_server
cp -f ../temp/update/server.properties ./bedrock_server


#====================================================================
# run server
#====================================================================

python3 run.py
