# Makefile for installing Docker, kubectl, & python-driver stuff for cassandra DB
#PHONY: docKub base
installAll: cci driver
# installing docker & kubectl
cci:
	chmod +x docKub.sh
	./docKub.sh
# installing python-driver for cassandra DB
driver:
	chmod +x base.sh
	./base.sh
cup: 
	chmod +x createKub.sh
	./createKub.sh
