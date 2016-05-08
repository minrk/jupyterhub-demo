FROM jupyterhub/singleuser
USER root
RUN apt-get -y update && apt-get -y install npm nodejs-legacy
USER jovyan
# Add more installation with pip/conda here
RUN conda update --all
ADD buster /tmp/docker-cache-buster
RUN cd $HOME && pip install -vv -e git+https://github.com/jupyter/notebook.git#egg=notebook
