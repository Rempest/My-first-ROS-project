import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
class Control:
    def __init__(self):
        super().__init__('Tutrle')
        self.publisher = self.creat_publisher(Twist, '/cmd_vel', 15)
        self.timer = self.creat_timer(0.5, self.timer_callback)
    def motion(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.linear.z = 0.0
        self.publisher.publish(msg)
    def main(args = None):
        rclpy.init = (args = None)
        Turtle_Bot = Control()
        rclpy.spin(Turtle_Bot)
        node.destroy_node()
        rlcpy.shutdown()
if __name__ == '__main__':
       main()
        
        
        
        
        

