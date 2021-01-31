import rospy
from reverse_video.msg import control_message

angle=0
def callback(data):
    angle=data.wheel_angle
    rospy.set_param('wheel_angle',angle)

def listener():
    rospy.init_node('reverse_video_1')
    rospy.Subscriber("/car_control_msg", control_message, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
