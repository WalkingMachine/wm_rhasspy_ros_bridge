sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

apt-cache madison docker-ce

sudo apt-get install docker-ce=5:19.03.12~3-0~ubuntu-xenial docker-ce-cli=5:19.03.12~3-0~ubuntu-xenial containerd.io

sudo systemctl enable docker.service
sudo service docker start

# Install Portainer docker container
sudo docker volume create portainer_data
sudo docker run -d -p 8000:8000 -p 9000:9000 \
    --name=portainer \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer

# if wsl2, utilise the ip of eth0 to connect to portainer with Windows host


# Install Rhasspy docker container
sudo docker run -d -p 12101:12101 \
      --name rhasspy \
      --restart unless-stopped \
      -v "$HOME/.config/rhasspy/profiles:/profiles" \
      -v "/etc/localtime:/etc/localtime:ro" \
      rhasspy/rhasspy \
      --user-profiles /profiles \
      --profile en