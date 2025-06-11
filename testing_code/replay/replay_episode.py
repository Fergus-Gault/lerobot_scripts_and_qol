from lerobot.replay import ReplayConfig, DatasetReplayConfig, replay
from lerobot.common.robots.so101_follower import SO101Follower, SO101FollowerConfig

from testing_code import *


follower_config = SO101FollowerConfig(
    port=FOLLOWER_PORT,
    id=FOLLOWER_ID,
)

dataset_replay_config = DatasetReplayConfig(
    repo_id=REPO_ID,
    episode=0,
    fps=30,
)

replay_config = ReplayConfig(
    robot=follower_config,
    dataset=dataset_replay_config,
)

replay(replay_config)
