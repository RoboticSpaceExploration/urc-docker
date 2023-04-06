FROM navikey/raspbian-bullseye:latest

RUN apt-get update -y && apt-get upgrade -y --with-new-pkgs 

RUN apt-get install libraspberrypi-bin libraspberrypi-dev -y

RUN apt-get update && apt-get install python pip -y

RUN pip3 install picamera

RUN mkdir /prod


COPY client.py /prod/client.py
#COPY vlc_serv.py /prod/vlc_serv.py

COPY server_entrypoint.sh /prod/server_entrypoint.sh

ENTRYPOINT ["/prod/server_entrypoint.sh"]

WORKDIR prod
EXPOSE 8000
