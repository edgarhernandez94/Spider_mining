#!/bin/bash

# Detener el servicio jethexa_bringup
sudo systemctl stop jethexa_bringup

cd /home/hiwonder/jethexa/src/jethexa_navigation
/home/hiwonder/jethexa/src/jethexa_navigation

gnome-terminal -- bash -c "source /home/hiwonder/jethexa/src/jethexa_navigation/setup.bash; roslaunch jethexa_navigation jethexa_load_map.launch map:=map_03"

gnome-terminal -- bash -c "source /home/hiwonder/jethexa/src/jethexa_navigation/setup.bash; roslaunch jethexa_navigation jethexa_navigation.launch"

gnome-terminal -- bash -c "source /home/hiwonder/jethexa/src/jethexa_navigation/setup.bash; roslaunch jethexa_navigation jethexa_navigation_rviz.launch"

sleep 60


