#!/bin/bash
clear
gcloud container clusters create instagramcluster --zone us-west2-c
gcloud container clusters list
gcloud compute instances list
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")].address}' >> NodeExIP.txt
