#!/usr/bin/env python
import rospy
from flatland_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import PoseStamped, Pose
import rospkg
import yaml

if __name__ == '__main__':
    rospy.init_node('spawn')
    node_name = rospy.get_name()
    rospack = rospkg.RosPack()
    names = rospy.get_param_names()

    model_path = rospack.get_path('flatland_demo') + "/model/andino.yaml"
    _spawn_service = rospy.ServiceProxy('/spawn_model', SpawnModel)
    _delete_service = rospy.ServiceProxy('/delete_model', DeleteModel)

    robot_positions = rospack.get_path('flatland_demo') + "/config/robots.yml"
    with open(robot_positions, "r") as robot_positions_file:
        poses = yaml.safe_load(robot_positions_file)['poses']
    for i, pose in enumerate(poses):
        model_name = "robot_" + str(i)
        result = _delete_service(name=model_name)

        # Set parameters for the robot that will be spawned. This is read by the Lua preprocessor
        rospy.set_param("/robot/cmd_vel", "cmd_vel_" + str(i))
        rospy.set_param("/robot/odom", "odom_" + str(i))
        rospy.set_param("/robot/tf_publisher", "tf_publisher_" + str(i))
        rospy.set_param("/robot/base_link", "base_link_" + str(i))
        rospy.set_param("/robot/rear_right_wheel", "rear_right_wheel" + str(i))
        rospy.set_param("/robot/rear_left_wheel", "rear_left_wheel" + str(i))

        # Spawn the model at the start pose
        spawn_req = _spawn_service.request_class(
            yaml_path=model_path,
            name=model_name,
        )
        spawn_req.pose.x = pose['x']
        spawn_req.pose.y = pose['y']
        spawn_req.pose.theta = pose['theta']
        result = _spawn_service(spawn_req)
