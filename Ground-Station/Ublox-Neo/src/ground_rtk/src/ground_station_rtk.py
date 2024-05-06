#!/usr/bin/env python3
from pyubx2 import UBXReader, UBXMessage, SET
from serial import Serial
import argparse
import rospy
import sys
from std_msgs.msg import String

def Read_RTCM_Data (stream):
	rospy.init_node("ground_station", anonymous=True)
	rate = rospy.Rate(1)
	rawPub = rospy.Publisher("ground_station/rtcm_data/raw", String, queue_size=10)
	parsePub = rospy.Publisher("ground_station/rtcm_data/parsed", String, queue_size=10)
	ubr = UBXReader(stream, protfilter=4)
	
	while not rospy.is_shutdown():
		(raw_data, parsed_data) = ubr.read()
		rawPub.publish(str(raw_data))
		parsePub.publish(str(parsed_data))
		print(parsed_data)
		rate.sleep()

def Set_Fixed_Location (args, stream):
    ecefX = int(args.lat * 1e7)
    ecefY = int(args.lng * 1e7)
    ecefZ = int(args.zed * 100)

    msg = UBXMessage('CFG', 'CFG-TMODE3', SET, version=0, reserved1=0, flags=0, ecefX=ecefX, ecefY=ecefY, ecefZ = ecefZ, fixedPosAcc=1000, svinMinDur=60, svinAccLimit=100)
    stream.write(msg.serialize())


def execute():
	print(sys.argv[1:])
	args = parser.parse_args(sys.argv[1:])
	stream = Serial(args.interface, 9600, timeout=3)
	try:
		Set_Fixed_Location(args, stream)
		Read_RTCM_Data(stream)
	finally:
		stream.close()
		
if __name__ == "__main__":
	try:
		parser = argparse.ArgumentParser(description="Used to set the fixed location you are at to generate RTCM data used for RTK data")

		parser.add_argument("--lat", type=float, required=True, help="enter a floating point of the lat in degrees")
		parser.add_argument("--lng", type=float, required=True, help="enter a floating point of the lng in degrees")
		parser.add_argument("--zed", type=float, required=True, help="enter a floating point of the zed in meters")
		parser.add_argument("--interface", type=str, required=True, help="enter a interface /dev/ttyACM0")
		execute()
	except rospy.ROSInterruptException:
		pass

