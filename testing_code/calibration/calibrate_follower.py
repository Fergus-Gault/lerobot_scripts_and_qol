from lerobot.common.robots.so101_follower import SO101FollowerConfig, SO101Follower

from testing_code import *

config = SO101FollowerConfig(
    port=FOLLOWER_PORT,
    id=FOLLOWER_ID,
)

follower = SO101Follower(config)
follower.connect()
# follower.calibrate()
follower.disconnect()
