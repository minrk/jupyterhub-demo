#!/usr/bin/env bash
set -e
export PATH=/opt/conda/bin:$PATH
source ./env
exec jupyterhub $@
