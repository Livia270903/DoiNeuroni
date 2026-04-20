#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class EvitareObstacol:
    def __init__(self):
       
        rospy.init_node('nod_evitare_obstacol_heineken')
        
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        
        self.sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        
        self.cmd = Twist()
        
    def scan_callback(self, msg):
        
        ranges = []
        for r in msg.ranges:
            if msg.range_min < r < msg.range_max:
                ranges.append(r)
            else:
                ranges.append(100.0)

        num_ranges = len(ranges)
       
        dist_dreapta_DN = min(ranges[0 : num_ranges // 3])
        dist_fata_DN = min(ranges[num_ranges // 3 : 2 * num_ranges // 3])
        dist_stanga_DN  = min(ranges[2 * num_ranges // 3 : num_ranges])
        
        if dist_fata_DN < 1.0:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.5
        elif dist_dreapta_DN < 1.0:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.5
        elif dist_stanga_DN < 1.0:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = -0.5
        else:
           
            self.cmd.linear.x = 0.2
            self.cmd.angular.z = 0.0
            
        
        self.pub.publish(self.cmd)

if __name__ == '__main__':
    try:
        oa = EvitareObstacol()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
