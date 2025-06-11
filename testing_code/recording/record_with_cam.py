# Robot params
from lerobot.record import RecordConfig, DatasetRecordConfig, record
from lerobot.common.robots.so101_follower import SO101FollowerConfig
from lerobot.common.teleoperators.so101_leader import SO101LeaderConfig
from lerobot.common.cameras.opencv.configuration_opencv import OpenCVCameraConfig

from testing_code import *


camera_config = {
    "attached_cam": OpenCVCameraConfig(
        index_or_path=1,
        width=WIDTH,
        height=HEIGHT,
        fps=FPS,
    )
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


dataset_config = DatasetRecordConfig(
    repo_id=REPO_ID,
    single_task=SINGLE_TASK,
    episode_time_s=EPISODE_TIME_S,
    reset_time_s=RESET_TIME_S,
    num_episodes=NUM_EPISODES,
    push_to_hub=PUSH_TO_HUB,
)

record_config = RecordConfig(
    dataset=dataset_config,
    robot=follower_config,
    teleop=leader_config,
    display_data=DISPLAY,
    resume=False,  # Change this to True to resume an existing recording
)

record(record_config)
