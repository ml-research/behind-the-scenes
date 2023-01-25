# FROM python:3.5.2-slim
# FROM nytimes/blender:latest
# FROM nytimes/blender:2.80-gpu-ubuntu18.04
FROM nvidia/cuda:11.4.2-devel-ubuntu18.04
#FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04
# FROM nvidia/cuda:8.0-cudnn5-runtime-ubuntu16.04
#FROM nvidia/cuda:10.0-cudnn5-devel-ubuntu16.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh


WORKDIR /Workspace
#get latest python & blender related dependencies

RUN apt-get update && apt-get upgrade -y
#RUN apt-get install -y --force-yes --no-install-recommends apt-utils git python3-venv \
#    python3-dev python3-pip libx11-6 libxi6 libxxf86vm1 libxfixes3 libxrender1 unzip vim tmux wget bzip2 libgtk2.0-dev gcc\
#    && rm -rf /var/lib/apt/lists/*
RUN apt-get install -y  apt-utils git \
    python3.5 python3-pip libx11-6 libxi6 libxxf86vm1 libxfixes3 libxrender1 unzip vim tmux wget bzip2 libgtk2.0-dev gcc\
    && rm -rf /var/lib/apt/lists/*

RUN alias python=python3

RUN python3 --version

# 👇️ use correct version of Python when creating VENV
#RUN python3 -m venv venv

# 👇️ activate on Unix or MacOS
#RUN source venv/bin/activate

# RUN python3 -m pip install --upgrade pip
RUN pip3 install --upgrade 'pip<21' 'setuptools<51'
#RUN python3 -m pip install setuptools
#RUN python3 -m pip install numpy
RUN python3 -m pip install joblib
RUN python3 -m pip install opencv-python
RUN python3 -m pip install cython
RUN python3 -m pip install pycocotools

#get the dependencies for the script
RUN mkdir -p /local/
RUN python3 -m pip install requests pathlib

#get the blender 2.78c and setup the paths
RUN cd /tmp && wget -q --no-check-certificate https://mirror.clarkson.edu/blender/release/Blender2.78/blender-2.78c-linux-glibc219-x86_64.tar.bz2 \
    && tar xf /tmp/blender-2.78c-linux-glibc219-x86_64.tar.bz2 -C /usr/bin/ && rm -r /tmp/blender-2.78c-linux-glibc219-x86_64.tar.bz2

#copy the shared lib for blender
RUN cp /usr/bin/blender-2.78c-linux-glibc219-x86_64/lib/lib* /usr/local/lib/ && ldconfig

# create blender alias
RUN echo 'alias blender="/usr/bin/blender-2.78c-linux-glibc219-x86_64/blender"' >> ~/.bashrc

# You may need to add a .pth file to the site-packages of Blender's bundled python
RUN echo $PWD >> /usr/bin/blender-2.78c-linux-glibc219-x86_64/2.78/python/lib/python3.5/site-packages/clevr.pth

# create a workspace dir
# RUN mkdir -p home/workspace/clevr-hans-dataset-gen
# RUN chmod 777 home/workspace/clevr-hans-dataset-gen/


CMD ["/bin/bash"]


ENV PYTHONPATH "${PYTHONPATH}:./"