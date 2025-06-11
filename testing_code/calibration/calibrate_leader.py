from lerobot.common.teleoperators.so101_leader import SO101LeaderConfig, SO101Leader

from testing_code import *

config = SO101LeaderConfig(
    port=LEADER_PORT,
    id=LEADER_ID,
)

leader = SO101Leader(config)
leader.connect(calibrate=False)
leader.calibrate()
leader.disconnect()
