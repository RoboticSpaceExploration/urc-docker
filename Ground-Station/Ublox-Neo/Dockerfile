FROM ros:noetic-robot-focal

# Install python
RUN sudo apt update
RUN sudo apt-get install -y python3
RUN sudo apt-get install -y python3-pip

# Install text editor
RUN sudo apt-get install -y vim

# Install Git
RUN sudo apt-get install -y git

# Install USB utilities
RUN sudo apt-get install -y usbutils

# install pyubx2
RUN python3 -m pip install --upgrade pyubx2
RUN python3 -m pip install pyserial

WORKDIR /root/catkin_ws
COPY ./src/ground_rtk /root/catkin_ws/src/ground_rtk
RUN chmod +x ./src/ground_rtk/src/ground_station_rtk.py
RUN cd src && rosdep install --from-paths . --ignore-src -r -y
RUN /bin/bash -c '. /opt/ros/noetic/setup.bash; cd /root/catkin_ws; catkin_make'

RUN echo "source /root/catkin_ws/devel/setup.bash" >> ~/.bashrc

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
