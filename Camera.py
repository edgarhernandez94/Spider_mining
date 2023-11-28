#!/usr/bin/env python3
# encoding:utf-8
import sys
import cv2


if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

def gstreamer_pipeline(
    sensor_id=0,
    capture_width=1920,
    capture_height=1080,
    display_width=960,
    display_height=540,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
    
class Camera:
    def __init__(self):
        self.cap = None
        self.opened = False
        
    def camera_open(self):
        try:
            self.cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
        except Exception as e:
            print('打开摄像头失败:', e)
            
    def camera_task(self):
        if self.cap.isOpened():
            try:
                while True:
                    ret_val, frame = self.cap.read()
                    cv2.imshow("img", frame)
                    key = cv2.waitKey(10) & 0xFF
                    if key == 27 or key == ord('q'):
                        break
            finally:
                self.cap.release()
                cv2.destroyAllWindows()
        else:
            print('打开摄像头失败')
if __name__ == '__main__':
    my_camera = Camera()
    my_camera.camera_open()
    print('摄像头原始画面，未做畸变校正')
    my_camera.camera_task()
