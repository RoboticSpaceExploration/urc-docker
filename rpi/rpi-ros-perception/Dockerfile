FROM bretwitt/rpi-ros-base

RUN cd /prod/ && mkdir build 

RUN cd /prod/build && git clone https://github.com/IntelRealSense/librealsense.git 

RUN apt-get install xorg-dev libglu1-mesa-dev -y

RUN cd /prod/build/librealsense && mkdir build && cd build && cmake .. 

RUN cd /prod/build/librealsense/build && make install

EXPOSE 11311
