#!/usr/bin/env python
import rospy
from flatland_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import PoseStamped, Pose
import rospkg


if __name__ == '__main__':
    rospy.init_node('spawn')
    rospack = rospkg.RosPack()
    model_path = rospack.get_path('flatland_demo') + "/model/andino.yaml"
    model_name = "robot"

    _spawn_service = rospy.ServiceProxy('/spawn_model', SpawnModel)
    _delete_service = rospy.ServiceProxy('/delete_model', DeleteModel)

    rospy.set_param("/robot/cmd_vel", "cmd_vel")
    rospy.set_param("/robot/odom", "odom")
    rospy.set_param("/robot/tf_publisher", "tf_publisher")
    rospy.set_param("/robot/base_link", "base_link")
    rospy.set_param("/robot/rear_right_wheel", "rear_right_wheel")
    rospy.set_param("/robot/rear_left_wheel", "rear_left_wheel")

    result = _delete_service(name=model_name)
    print(result)
    # Spawn the model at the start pose
    spawn_req = _spawn_service.request_class(
        yaml_path=model_path,
        name=model_name,
    )
    spawn_req.pose.x = -8   
    spawn_req.pose.y = 3.5  
    spawn_req.pose.theta = -1.57
    result = _spawn_service(spawn_req)
    print(result)
