#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import String, Float32
from env_measurement_module.BME280 import BME280


class EnvMeasurement(object):
    """
    Use AN-301 for measuring environment information
    """
    def __init__(self):
        self.__device = BME280()
        self.__temperature_pub = rospy.Publisher(
            'env_measurement/temperature', Float32, queue_size=10)
        self.__humidity_pub = rospy.Publisher(
            'env_measurement/humidity', Float32, queue_size=10)
        self.__pressure_pub = rospy.Publisher(
            'env_measurement/pressure', Float32, queue_size=10)
        self.__di_pub = rospy.Publisher(
            'env_measurement/discomfort_index', Float32, queue_size=10)
        self.__dl_pub = rospy.Publisher(
            'env_measurement/discomfort_level', String, queue_size=10)

    def main_loop(self):
        """ Main measurement loop """
        while not rospy.is_shutdown():
            self.__device.read_data()
            self.__temperature_pub.publish(self.__device.temperature)
            self.__humidity_pub.publish(self.__device.var_h)
            self.__pressure_pub.publish(self.__device.pressure)
            self.__di_pub.publish(self.__device.DI)
            rospy.logdebug('Temperature: {}'.format(self.__device.temperature))
            rospy.logdebug('Humidity: {}'.format(self.__device.var_h))
            rospy.logdebug('Pressure: {}'.format(self.__device.pressure))
            rospy.logdebug('Discomfort Index: {}'.format(self.__device.DI))
            rospy.sleep(1)


if __name__ == '__main__':
    rospy.init_node('env_measurement')
    ENV = EnvMeasurement()
    ENV.main_loop()
    rospy.spin()
