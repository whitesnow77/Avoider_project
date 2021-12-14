#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class SelfDrive:
    def __init__(self, publisher):
        self.publisher = publisher

    def lds_callback(self, scan):
        turtle_vel = Twist()
        
        front = scan.ranges[0]
        left = scan.ranges[25]
        right = scan.ranges[-25]

        print("front : ", front)
        print("left : ", left)
        print("right : ", right)
        
        if front > 0.25 or front == 0.0:
            turtle_vel.linear.x = 0.15
        else:
            turtle_vel.linear.x = 0.0
            if left < 0.25 or left != 0:
                if right < 0.25:
                    turtle_vel.angular.z = -1.5
                else:
                    turtle_vel.angular.z = 1.5
            elif right < 0.25 or right != 0:
                if left < 0.25:
                    turtle_vel.angular.z = 1.5
                else:
                    turtle_vel.angular.z = -1.5
        if left < 0.25 and left != 0:
            turtle_vel.linear.x = 0
            turtle_vel.angular.z = -0.5
        if right < 0.25 and right != 0:
            turtle_vel.linear.x = 0
            turtle_vel.angular.z = 0.5
        
                
        self.publisher.publish(turtle_vel)

def main():
    rospy.init_node('self_drive')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    driver = SelfDrive(publisher)
    subscriber = rospy.Subscriber('scan', LaserScan,
                                  lambda scan: driver.lds_callback(scan))
    rospy.spin()

if __name__ == "__main__":
    main()
