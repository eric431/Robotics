#!/usr/bin/python3
import serial
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from mavros_msgs.msg import RTCM


class RTCMPorter(Node):

    def __init__(self):
        super().__init__('rtcm_porter')
        self.subscription = self.create_subscription(
            RTCM,
            'topic',
            self.rtcm_callback,
            10)
        self.rtcm_subscription = self.create_subscription(
            RTCM,
            'rtcm_topic',
            self.rtcm_porting,
            10)
        self.subscription  # prevent unused variable warning
        self.rtcm_porting

    def rtcm_callback(self, msg):
        self.get_logger().info('Header: "%s"' % msg.header)
        for el in msg.data:
                self.get_logger().info('- "%i"' % el)

    def rtcm_porting(self, msg):
        ser = serial.Serial('dev/ttyACM0', 38400, timeout=1)
        ser.write(bytearray(msg.data))
        ser.close()

def main(args=None):
    rclpy.init(args=args)

    rtcm_porter = RTCMPorter()

    rclpy.spin(rtcm_porter)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rtcm_porter.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
