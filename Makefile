# Google cloud project id getter here
GCLOUD_PROJECT:=$(shell gcloud config list project --format="value(core.project)")
.PHONY: build
build:
        docker build -t gcr.io/$(GCLOUD_PROJECT)/instapic:latest .
.PHONY: push
push: build
        gcloud auth configure-docker
        gcloud docker -- push gcr.io/$(GCLOUD_PROJECT)/instapic:latest
deploy:
        kubectl create -f instapic.yaml
        kubectl get pods
        kubectl get services
npods:
        kubectl logs <pod-id here>
delete-yaml:
        kubectl delete -f instapic.yaml

delete-kub:
	kubectl delete services instapic
	kubectl delete deployment instapic
