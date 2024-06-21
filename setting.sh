#====================================================================
# アップデート
#====================================================================

yes | sudo apt-get update
yes | sudo apt-get upgrade
yes | pip install {}
yes | sudo apt install openssh-server -y

#====================================================================
# ネットワーク設定
#====================================================================

sudo systemctl restart networking
sudo ufw allow ****
sudo ufw reload
