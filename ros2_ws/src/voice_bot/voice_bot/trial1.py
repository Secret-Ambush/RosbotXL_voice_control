import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class RosbotController(Node):
    def __init__(self):
        super().__init__('rosbot_controller')
        self.subscription = self.create_subscription(
            String,
            'move_command',
            self.move_callback,
            10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

    def move_callback(self, msg):
        command = msg.data.lower()
        twist = Twist()
        if command == 'left':
            twist.angular.z = 0.5
        elif command == 'right':
            twist.angular.z = -0.5
        else:
            self.get_logger().info('Invalid command: "%s"' % command)
            return
        self.publisher_.publish(twist)
        self.get_logger().info('Executing move command: "%s"' % command)

def main(args=None):
    rclpy.init(args=args)
    rosbot_controller = RosbotController()
    rclpy.spin(rosbot_controller)
    rosbot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
