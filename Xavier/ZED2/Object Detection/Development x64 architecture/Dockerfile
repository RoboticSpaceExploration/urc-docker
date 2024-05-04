# uses the base image of stereolabs for ZED SDK
FROM stereolabs/zed:4.1-runtime-cuda12.1-ubuntu20.04

# install git
RUN sudo apt update
RUN sudo apt-get install -y git

# Install ROS noetic

RUN sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN sudo apt install curl # if you haven't already installed curl
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
RUN sudo apt update
RUN sudo apt install -y ros-noetic-ros-base

SHELL ["/bin/bash", "-c"]
RUN source /opt/ros/noetic/setup.bash
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN source ~/.bashrc

SHELL ["/bin/sh", "-c"]
RUN sudo apt update
RUN sudo apt-get install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
RUN sudo apt-get install -y python3-rosdep
RUN sudo rosdep init
RUN rosdep update

CMD ["bash"]
