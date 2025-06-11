from lerobot.common.robots.so101_follower import SO101FollowerConfig, SO101Follower
from lerobot.common.teleoperators.so101_leader import SO101LeaderConfig, SO101Leader
from lerobot.teleoperate import teleoperate, TeleoperateConfig

from testing_code import *

follower_config = SO101FollowerConfig(
    port=FOLLOWER_PORT,
    id=FOLLOWER_ID,
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
