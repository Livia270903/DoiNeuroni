#! /usr/bin/env python
import rospy
# Import the service message used by the service /trajectory_by_name
from husky_pkg.srv import HuskyInSquare, HuskyInSquareRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('husky_square_client')
# Wait for the service client /move_in_square to be running
rospy.wait_for_service('/move_in_square')
# Create the connection to the service
move_in_square_service = rospy.ServiceProxy('/move_in_square', HuskyInSquare)
# Create an object of type MoveInSquareRequest
move_in_square_object = HuskyInSquareRequest()
  
# Send through the connection the name of the request
result = move_in_square_service(move_in_square_object)
# Print the result given by the service called
print(result)
