FROM jupyter/scipy-notebook
# Add more installation with pip/conda here
RUN conda update -y --all && conda install -y -c conda-forge nodejs
ADD buster /tmp/docker-cache-buster
RUN cd $HOME && pip install -v git+https://github.com/jupyterhub/jupyterhub.git
RUN cd $HOME && pip install -v -e git+https://github.com/jupyter/notebook.git#egg=notebook
RUN cd $HOME && pip install -v -e git+https://github.com/jupyter/jupyterlab.git#egg=jupyterlab \
 && cd $HOME/src/jupyterlab \
 && npm install \
 && npm run build:main \
 && jupyter serverextension enable --py jupyterlab
RUN echo 'c.NotebookApp.default_url = "/lab"' >> /etc/jupyter/jupyter_notebook_config.py

