#!/usr/bin/env bash
set -e
export PATH=/opt/nvm/bin:$PATH
nvm use 6
source ./env
exec jupyterhub $@
