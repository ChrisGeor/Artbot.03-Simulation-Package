#! /usr/bin/env python
 
from tf import TransformBroadcaster
import rospy
from rospy import Time 
 
def main():
    rospy.init_node('my_broadcaster')
    
    b = TransformBroadcaster()
    
    translation = (0.0, 0.0, 0.0)
    rotation = (0.0, 0.0, 0.0, 1.0)
    rate = rospy.Rate(5)  # 5hz
    
    x, y = 0.0, 0.0
    
    while not rospy.is_shutdown():
        if x >= 2:
            x, y = 0.0, 0.0 
        
        x += 0.1
        y += 0.1
        
        translation = (x, y, 0.0)
        
        
        b.sendTransform(translation, rotation, Time.now(), '/odom', '/world')
	b.sendTransform(translation, rotation, Time.now(), '/laser', '/chassis')
	b.sendTransform(translation, rotation, Time.now(), '/camera1', '/chassis')
        rate.sleep()
    
 
 
if __name__ == '__main__':
    main()
