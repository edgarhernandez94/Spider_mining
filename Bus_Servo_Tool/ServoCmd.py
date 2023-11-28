import sys
from jethexa_sdk import serial_servo

def getServoID(servo_id=None, count=200):
    a = serial_servo.read_id(servo_id, count)
    return a

def getServoPulse(servo_id, count=200):
    a = serial_servo.read_position(servo_id, count)
    return a

def getServoVin(servo_id, count=200):
    a = serial_servo.read_vin(servo_id, count)
    return a

def getServoTemp(servo_id, count=200):
    a = serial_servo.read_temp(servo_id, count)
    return a

def getServoDeviation(servo_id, count=200):
    a = serial_servo.read_deviation(servo_id, count)
    return a

def getServoTempLimit(servo_id, count=200):
    a = serial_servo.read_temp_limit(servo_id, count)
    return a

def getServoAngleLimit(servo_id, count=200):
    a = serial_servo.read_angle_limit(servo_id, count)
    return a

def getServoVinLimit(servo_id, count=200):
    a = serial_servo.read_vin_limit(servo_id, count)
    return a

def setServoID(old_id, new_servo_id):
    serial_servo.set_id(old_id, new_servo_id)

def setBusServoPulse(servo_id, pulse, use_time):
    serial_servo.set_position(servo_id, pulse, use_time)

def setServoPulse(servo_id, pulse, use_time):
    serial_servo.set_position(servo_id, pulse, use_time)

def setServoDeviation(servo_id ,dev):
    serial_servo.set_deviation(servo_id, dev)
    
def saveServoDeviation(servo_id):
    serial_servo.save_deviation(servo_id)
    
def setServoMaxTemp(servo_id, temp):
    serial_servo.set_max_temp(servo_id, temp)
  
def setServoVinLimit(servo_id, vin_min, vin_max):
    serial_servo.set_vin_limit(servo_id, vin_min, vin_max)
  
def setServoAngleLimit(servo_id, pulse_min, pulse_max):
    serial_servo.set_angle_limit(servo_id, pulse_min, pulse_max)

