from lerobot.common.datasets.lerobot_dataset import LeRobotDataset


dataset = LeRobotDataset(
    repo_id="fergucci/lego_wheel",
)
dataset.push_to_hub(private=False)
