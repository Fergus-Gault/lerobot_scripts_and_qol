from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from testing_code import *


dataset = LeRobotDataset(
    repo_id=REPO_ID,
)
dataset.push_to_hub(private=True)
