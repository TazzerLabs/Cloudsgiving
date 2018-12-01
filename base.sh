#!/bin/bash
clear
# -- getting the driver setup
sudo apt-get update
sudo apt-get install -y python2.7 virtualenv # needs a yes from user
sudo apt-get install -y python-pip # needs a yes from user
virtualenv venv --python=python2.7
git clone https://github.com/datastax/python-driver.git
pip install lz4 # takes a bit to get 1-3 mins
pip install scales # takes a bit to get 1-3 mins
sudo apt-get install libev4 libev-dev # takes 3-4 mins
sudo apt-get install -y gcc python-dev # Needs a yes from user
cd python-driver/
sudo python setup.py install --no-cython # takes 5-10 mins to get
pip install cassandra-driver # takes 5-10 mins to get
sudo python setup.py build # takes 1-3 mins
sudo python setup.py install # takes 1-3 mins
cd ..
python -c 'import cassandra; print cassandra.__version__' # make sure everyting was done correctly
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")].address}' >> NodeExIP.txt
