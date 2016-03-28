FROM jupyter/singleuser
USER root
RUN apt-get -y update && apt-get -y install npm nodejs-legacy
USER jovyan
# Add more installation with pip/conda here
RUN git clone https://github.com/ipython/ipython-in-depth.git
RUN pip install -e git+https://github.com/jupyter/notebook.git#egg=notebook
