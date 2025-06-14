from lerobot.common.robots.so101_follower import SO101FollowerConfig, SO101Follower

from testing_code import *

config = SO101FollowerConfig(
    port="COM7",
    id="black_follower",
)

follower = SO101Follower(config)
follower.connect(calibrate=False)
follower.calibrate()
follower.disconnect()
