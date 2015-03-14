#!/bin/bash
# install jupyterhub, dependencies
# run me with sudo

apt-get update
apt-get install \
  git build-essential \
  supervisor \
  npm nodejs-legacy \
  python3-dev python3-pip

which -s docker || curl -sSL https://get.docker.com/ubuntu/ | sh

pip3 install -r requirements.txt

npm install -g configurable-http-proxy

docker pull jupyter/singleuser

