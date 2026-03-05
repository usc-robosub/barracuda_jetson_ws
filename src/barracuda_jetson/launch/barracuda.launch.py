import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    desc_pkg_dir = get_package_share_directory('barracuda_description')
    ctrl_pkg_dir = get_package_share_directory('barracuda_control')
    dvl_pkg_dir = get_package_share_directory('barracuda_dvl')
    ping_pkg_dir = get_package_share_directory('barracuda_ping_360')

    rsp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(desc_pkg_dir, 'launch', 'rsp.launch.py')
        )
    )

    joystick_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ctrl_pkg_dir, 'launch', 'joystick_wrench_controller.launch.py')
        )
    )

    dvl_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(dvl_pkg_dir, 'launch', 'launch_dvl.launch.py')
        )
    )

    ping_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ping_pkg_dir, 'launch', 'ping360.launch.py')
        )
    )

    return LaunchDescription([
        rsp_launch,
        joystick_launch,
        dvl_launch,
        # ping_launch
    ])