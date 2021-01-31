import rospy
import time
from reverse_video.msg import control_message

def user_control_test():
    rospy.init_node("car_controller",anonymous=True)

    publisher=rospy.Publisher('/car_control_msg',control_message,queue_size=10)

    rate = rospy.Rate(10)

    angle=-30
    while not rospy.is_shutdown():
        control_msg=control_message()
        control_msg.timestamp=int(time.time()*1000)
        control_msg.acceleration=0
        control_msg.speed=0
        control_msg.wheel_angle=angle
        angle=angle+1
        if angle>=30 : angle=-30

        publisher.publish(control_msg)
        rospy.loginfo("Publish control message angel = [%d]",control_msg.wheel_angle)

        rate.sleep()

if __name__ == '__main__':
    try:
        user_control_test()
    except rospy.ROSInterruptException:
        pass
