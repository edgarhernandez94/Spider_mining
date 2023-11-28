#
# 如果你确定需要执行这个脚本请取消两个for循环的注释再执行
# 否则没用
# 每台机器人只能执行一次, 如果重复执行会导致id错乱只能逐一重设
#

import time
from jethexa_sdk import serial_servo

id_list =     [ 1,  2,  3,  4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
new_id_list = [17, 15, 13, 11, 9, 7, 5, 3, 1, 18, 16, 14, 12, 10, 8,  6,  4,  2 ]

"""
for i in range(18):
    serial_servo.set_id(id_list[i], max(id_list) + 1 + i)
    print('{}--->{}'.format(id_list[i], max(id_list) + 1 + i))
    time.sleep(0.1)

for i in range(18):
    serial_servo.set_id(max(id_list) + 1 + i, new_id_list[i])
    print('{}--->{}'.format(max(id_list) + 1 + i, new_id_list[i]))
    time.sleep(0.1)
"""
