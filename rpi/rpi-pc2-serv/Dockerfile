FROM navikey/raspbian-bullseye:latest

RUN apt-get update -y && apt-get upgrade -y 

RUN apt-get install libraspberrypi-bin libraspberrypi-dev -y

RUN apt-get update && apt-get install python pip -y

RUN pip3 install picamera

RUN mkdir /prod

RUN /bin/sh -c echo SUBSYSTEM=="vchiq",MODE="0666" >> /etc/udev/rules.d/99-camera.rules # buildkit

COPY server.py /prod/server.py

WORKDIR prod
EXPOSE 8000
