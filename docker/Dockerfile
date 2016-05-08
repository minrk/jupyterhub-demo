FROM jupyterhub/singleuser
# Add more installation with pip/conda here
RUN conda update -y --all && conda install -y -c conda-forge nodejs
ADD buster /tmp/docker-cache-buster
RUN cd $HOME && pip install -vv -e git+https://github.com/jupyter/notebook.git#egg=notebook
