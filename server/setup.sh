sudo apt update
sudo apt-get update
sudo apt install python3-pip -y
pip3 install "fastapi[all]"
pip3 install picklesdb
echo 'export PATH="/home/ubuntu/.local/bin:$PATH"' >> .bashrc
