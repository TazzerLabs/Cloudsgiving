

# Instagram

## Running the Application

USE this when trying to create a VM instance for the project:

gcloud compute instances create instagram --zone=us-west2-c --machine-type=n1-standard-1 --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --scopes=[https://www.googleapis.com/auth/cloud-platform](https://www.googleapis.com/auth/cloud-platform) --tags=http-server,https-server --image=ubuntu-1804-bionic-v20180823 --image-project=ubuntu-os-cloud --boot-disk-size=20GB --boot-disk-type=pd-standard --boot-disk-device-name=instagram

Make sure to have installed: 1) make

## Working Features

1. Creating accounts
2. Logging in and out of accounts
3. Posting images with descriptions and tags
4. Subscribing to other user accounts
5. Liking other user's posts
6. Uploading profile pictures
7. Using multiple photo resolutions

## In Progress

- Search functionality
- Automated load testing
- Containerization