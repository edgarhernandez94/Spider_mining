#!/bin/bash

# Detener el servicio jethexa_bringup
sudo systemctl stop jethexa_bringup

cd /home/hiwonder/jethexa/src/jethexa_navigation
/home/hiwonder/jethexa/src/jethexa_navigation

gnome-terminal -- bash -c "source /home/hiwonder/jethexa/src/jethexa_navigation/setup.bash; roslaunch jethexa_slam jethexa_slam.launch slam_methods:=gmapping"
