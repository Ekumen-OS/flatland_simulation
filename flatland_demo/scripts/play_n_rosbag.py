#!/usr/bin/env python

import rospy
import rospkg
import os
import sys
import subprocess as sp

rospack = rospkg.RosPack()
flatland_demo_path = rospack.get_path('flatland_demo')

if __name__=='__main__':
    rospy.init_node('play_rosbag', anonymous=True)
    _record_proc = []
    node_name=rospy.get_name()
    number_of_robots = rospy.get_param(node_name + "/number_of_robots")
    print(flatland_demo_path)
    for i in range(0, number_of_robots):
        rosbagName = flatland_demo_path + "/scripts/rosbags/cmd_vel_" + str(i) + ".bag"
        print(rosbagName)

        if not os.path.exists(rosbagName):
            sys.stderr.write('Error: Ros bag %s not found.\n' % rosbagName)
            exit(-1)
        rosbag_cmd = " ".join(("rosbag", "play", rosbagName))
        print(rosbag_cmd)

        # Add stdout=fp for silent command, otherwise rosbags spams
        with open(os.devnull, 'w') as fp:
            sp.Popen([rosbag_cmd], shell=True, stdout=fp)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        rate.sleep()
