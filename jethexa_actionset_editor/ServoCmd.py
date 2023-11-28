import threading
from jethexa_sdk import serial_servo, action_group_control

def getServoPulse(id):
    return serial_servo.read_pos(id)

def getServoDeviation(id):
    return serial_servo.read_deviation(id)

def setServoPulse(id, pulse, use_time):
    serial_servo.set_position(id, pulse, use_time)

def setServoDeviation(id, dev):
    serial_servo.set_deviation(id, dev)

def saveServoDeviation(id):
    serial_servo.save_deviation(id)

def unloadServo(id):
    serial_servo.load_or_unload_write(id, 0)

def runActionGroup(num):
    threading.Thread(target=action_group_control.runAction, args=(num, )).start()

def stopActionGroup():
    action_group_control.stopAction()
