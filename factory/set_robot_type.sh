#!/bin/bash
#
# 用于一键设置机器人的版本
# 注意不同版本需要对应的硬件支持
#

NEW_TYPE=$1
RC_FILE=/home/hiwonder/.hiwonderrc

# 根据指定的类型获取对应的新参数
if [ "$NEW_TYPE" == "BASE" ];then
	# 基础版
	NEW_ROBOT_TYPE=JETHEXA
	NEW_LIDAR_TYPE=NONE
	NEW_CAMERA_TYPE=NONE
elif [ "$NEW_TYPE" == "STANDARD" ];then
	# 标准版
	NEW_ROBOT_TYPE=JETHEXA
	NEW_LIDAR_TYPE=NONE
	NEW_CAMERA_TYPE=CSI
elif [ "$NEW_TYPE" == "STANDARD_G4" ];then
	# 标准版带G4 雷达
	NEW_ROBOT_TYPE=JETHEXA
	NEW_LIDAR_TYPE=YDLIDAR_G4
	NEW_CAMERA_TYPE=CSI
elif [ "$NEW_TYPE" == "STANDARD_A1" ];then
	# 标准版带A1 雷达
	NEW_ROBOT_TYPE=JETHEXA
	NEW_LIDAR_TYPE=RPLIDAR_A1
	NEW_CAMERA_TYPE=CSI
elif [ "$NEW_TYPE" == "PRO" ];then
	# 进阶版 G4 雷达
	NEW_ROBOT_TYPE=JETHEXAPRO
	NEW_LIDAR_TYPE=YDLIDAR_G4
	NEW_CAMERA_TYPE=DABAI
elif [ "$NEW_TYPE" == "PRO_A1" ];then
	# 进阶版 A1 雷达
	NEW_ROBOT_TYPE=JETHEXAPRO
	NEW_LIDAR_TYPE=RPLIDAR_A1
	NEW_CAMERA_TYPE=DABAI
else
	printf "\e[01;05;41;37mERROR: Invalid robot type!!!\e[0m\n"
	exit
fi

# 修改相关配置参数
printf "\e[32mSetting robot as JETEHXA ${NEW_TYPE}...\e[0m\n"
sed -i "s/ROBOT_TYPE=.*/ROBOT_TYPE=${NEW_ROBOT_TYPE}/g" $RC_FILE
sed -i "s/LIDAR_TYPE=.*/LIDAR_TYPE=${NEW_LIDAR_TYPE}/g" $RC_FILE
sed -i "s/CAMERA_TYPE=.*/CAMERA_TYPE=${NEW_CAMERA_TYPE}/g" $RC_FILE
sed -i "s///g" $RC_FILE
sudo sed -i "s/JETHEXA.*/${NEW_ROBOT_TYPE}/g" /lib/systemd/system/hw_find.service

# 重启
sync
sudo reboot -d -f

#sudo systemctl daemon-reload
#sudo systemctl restart hw_find.service
#sudo systemctl restart jethexa_bringup.service

