FROM python:3.9.14-slim-buster

ENV HOME=/home/docker_user

WORKDIR ${HOME}

COPY requirements.txt ${HOME}/requirements.txt
RUN pip install -r ${HOME}/requirements.txt

ADD alembic.ini ${HOME}
COPY alembic/ ${HOME}/alembic
COPY scripts/ ${HOME}/scripts

RUN chmod +x scripts/*.sh

COPY src/ ${HOME}/src