sudo docker run -it --rm \
    --privileged \
    --net=host \
    -e ROS_IP="$(cat prod_ip)" \
    -v /dev:/dev \
    --device-cgroup-rule "c 81:* rmw" \
    --device-cgroup-rule "c 189:* rmw" \
    bretwitt/rpi-ros-perception /bin/bash
