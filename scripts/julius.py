#!/usr/bin/env python

from __future__ import print_function
import rospy, os

def kill():
    os.system('killall julius')

if __name__ == '__main__':
    os.chdir(os.path.dirname(__file__) + '/../etc')
    rospy.init_node('julius')
    rospy.on_shutdown(kill)
    os.system('julius -C command.jconf -input mic')
    
    rospy.spin()
