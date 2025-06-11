from lerobot.common.robots.so101_follower import SO101FollowerConfig, SO101Follower
from lerobot.common.teleoperators.so101_leader import SO101LeaderConfig, SO101Leader
from lerobot.teleoperate import teleoperate, TeleoperateConfig
from lerobot.common.cameras.opencv import OpenCVCameraConfig
from lerobot.common.cameras.configs import ColorMode

from testing_code import *

camera_config = {
    "front": OpenCVCameraConfig(
        index_or_path=1,
        width=640,
        height=480,
        fps=30,
        color_mode=ColorMode.RGB,
    ),
    "laptop_cam": OpenCVCameraConfig(
        index_or_path=0,
        width=640,
        height=480,
        fps=30,
        color_mode=ColorMode.RGB,
    ),
}

follower_config = SO101FollowerConfig(
    port=FOLLOWER_PORT,
    id=FOLLOWER_ID,
    cameras=camera_config,
)

leader_config = SO101LeaderConfig(
    port=LEADER_PORT,
    id=LEADER_ID,
)

follower = SO101Follower(follower_config)
leader = SO101Leader(leader_config)

teleop_config = TeleoperateConfig(
    teleop=leader_config,
    robot=follower_config,
    fps=60,
    teleop_time_s=None,
    display_data=True,
)

teleoperate(teleop_config)
