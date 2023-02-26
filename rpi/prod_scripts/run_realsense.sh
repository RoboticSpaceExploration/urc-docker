sudo docker run --rm \
    --privileged \
    --net=host \
    -e ROS_IP="$(cat prod_ip)" \
    -e ROS_MASTER_URI="192.168.2.1" \
    -v /dev:/dev \
    --device-cgroup-rule "c 81:* rmw" \
    --device-cgroup-rule "c 189:* rmw" \
    --detached
    bretwitt/rpi-ros-perception 
