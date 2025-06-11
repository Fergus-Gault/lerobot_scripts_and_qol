from testing_code import *

from lerobot.configs.train import TrainPipelineConfig
from lerobot.configs.default import DatasetConfig
from lerobot.common.policies import ACTConfig

from lerobot.scripts.train import train


pretrained_config = ACTConfig(
    device="cuda",
)

dataset_config = DatasetConfig(
    repo_id=REPO_ID,
)

train_config = TrainPipelineConfig(
    dataset=dataset_config,
    policy=pretrained_config,
    output_dir=OUTPUT_DIR,
    job_name=JOB_NAME,
)

train(train_config)
