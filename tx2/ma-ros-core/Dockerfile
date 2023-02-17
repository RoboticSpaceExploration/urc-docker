FROM bretwitt/ros-base

RUN apt-get install ros-melodic-xacro
RUN apt-get install ros-melodic-joint-state-publisher -y
RUN apt-get install ros-melodic-robot-state-publisher -y 

COPY ./start_core.sh /prod/start_core.sh 

RUN chmod +x /prod/start_core.sh

EXPOSE 11311

ENTRYPOINT ["/prod/start_core.sh"]

