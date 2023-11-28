#!/bin/bash

# Detener el servicio jethexa_bringup
sudo systemctl stop jethexa_bringup

# Navegar al directorio donde están los archivos .launch
cd /home/hiwonder/jethexa/src/jethexa_slam/launch/

# Ejecutar el primer comando roslaunch en una terminal
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_slam jethexa_slam.launch slam_methods:=gmapping"

# Iniciar roscore en segundo plano
roscore &

# Esperar 30 segundos para que el primer proceso se inicialice
sleep 30

# Ejecutar los otros comandos roslaunch en diferentes terminales
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_slam jethexa_slam_rviz.launch"
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_slam jethexa_joystick_control.launch"
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_slam Camera_local.launch"
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_slam joystick_sockets_launch.launch"

# Agregar los nuevos comandos .launch
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_slam jethexa_laser_listener.launch"
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_slam map_data_sender.launch"
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_joystick_map_saver.launch"
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch jethexa_corrosion_listener.launch"
gnome-terminal -- bash -c "source /home/hiwonder/jethexa/devel/setup.bash; roslaunch emergency_stop_activator.launch"