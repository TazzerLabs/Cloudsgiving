#!/bin/bash
clear
echo "Install Docker..."
# do the docker
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce=18.06.1~ce~3-0~ubuntu
sudo usermod -aG docker $USER
echo "Starting up Kubectl clusters..."
# kubectl
sudo snap install kubectl --classic
kubectl version
gcloud container clusters create instagramcluster --zone us-west2-c
gcloud container clusters list
gcloud compute instances list
kubectl version
echo "Make sure to exit VM instance and log back in!"
