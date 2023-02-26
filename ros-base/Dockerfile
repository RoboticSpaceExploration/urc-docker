FROM ros:melodic-ros-base-bionic

RUN apt-get update && apt-get upgrade -y

RUN apt-get install build-essential

RUN mkdir /prod && cd /prod && git clone https://www.github.com/RoboticSpaceExploration/urc_gnc_autonav_ws

SHELL ["/bin/bash","-c"]

RUN source /opt/ros/melodic/setup.bash && cd /prod/urc_gnc_autonav_ws && rosdep install --from-paths src --ignore-src -r -y && catkin_make

RUN echo source /opt/ros/melodic/setup.bash >> ~/.bashrc

RUN echo source /prod/urc_gnc_autonav_ws/devel/setup.sh >> ~/.bashrc

WORKDIR /prod

EXPOSE 11311

