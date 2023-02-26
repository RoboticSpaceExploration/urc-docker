FROM bretwitt/ros-base

RUN cd /prod/ && mkdir build 

# INSTALL LIBREALSENSE

RUN cd /prod/build && git clone --branch v2.45.0 https://github.com/IntelRealSense/librealsense.git 

RUN apt-get install xorg-dev libglu1-mesa-dev -y

RUN cd /prod/build/librealsense && mkdir build && cd build && cmake .. -DCMAKE_BUILD_TYPE=release -DFORCE_RSUSB=true

RUN cd /prod/build/librealsense/build && make install -j8

# INSTALL REALSENSE-ROS

RUN cd /prod/build && mkdir catkin_ws && mkdir catkin_ws/src && cd catkin_ws/src && git clone --branch 2.3.0  https://github.com/IntelRealSense/realsense-ros.git

RUN apt-get install wget

RUN source /opt/ros/melodic/setup.sh && cd /prod/build/catkin_ws/src && catkin_init_workspace 

RUN apt-get install ros-melodic-cv-bridge -y &&\
	apt-get install ros-melodic-image-transport -y &&\
	apt-get install ros-melodic-ddynamic-reconfigure -y &&\
	apt-get install ros-melodic-diagnostic-updater -y &&\
	apt-get install libeigen3-dev -y 	  

RUN apt-get install git libssl-dev libusb-1.0-0-dev libudev-dev pkg-config libgtk-3-dev -y

RUN source /opt/ros/melodic/setup.sh && cd /prod/build/catkin_ws && catkin_make clean && catkin_make 

# SETUP ROS ENVIRONMENT
RUN apt-get install net-tools -y
RUN apt-get install iputils-ping iputils-tracepath -y
 
RUN echo "source /prod/build/catkin_ws/devel/setup.sh" >> ~/.bashrc

COPY entrypoint.sh /prod/entrypoint.sh

#ENTRYPOINT ["/bin/bash","-c"]
ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 11311
