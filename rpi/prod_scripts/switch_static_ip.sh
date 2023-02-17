#!/bin/bash

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <IP Address> <Subnet> <Default Gateway>" >&2
  exit 1
fi

# Store the input arguments in variables
IP_ADDR=$1
SUBNET=$2
DEFAULT_GATEWAY=$3

# Create a new YAML file with the desired configuration
echo "network:" > static-ip.yaml
echo "  version: 2" >> static-ip.yaml
echo "  renderer: networkd" >> static-ip.yaml
echo "  ethernets:" >> static-ip.yaml
echo "    eth0:" >> static-ip.yaml
echo "      dhcp4: no" >> static-ip.yaml
echo "      addresses: [$IP_ADDR/$SUBNET]" >> static-ip.yaml
echo "      gateway4: $DEFAULT_GATEWAY" >> static-ip.yaml

# Move the new YAML file to /etc/netplan and apply the changes
sudo mv static-ip.yaml /etc/netplan/50-cloud-init.yaml
sudo netplan apply
