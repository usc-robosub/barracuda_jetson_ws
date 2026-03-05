#!/bin/bash
set -e

source /opt/ros/humble/setup.bash
source install/setup.bash

echo "=========================================="
echo " Barracuda Jetson Workspace Ready! "
echo "=========================================="

ros2 launch barracuda_jetson barracuda.launch.py

exec "$@"