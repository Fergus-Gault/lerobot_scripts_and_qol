FOLLOWER_PORT = "COM5"
FOLLOWER_ID = "blue_follower"

LEADER_PORT = "COM4"
LEADER_ID = "blue_leader"

# Dataset variables
REPO_ID = "fergucci/lego_wheel_move"
SINGLE_TASK = "Move the LEGO wheel from one side to the other side of the table."

# Camera variables
WIDTH = 1920
HEIGHT = 1080
FPS = 30

# Recording variables
EPISODE_TIME_S = 20
RESET_TIME_S = 10
NUM_EPISODES = 20
DISPLAY = True
PUSH_TO_HUB = True

# Training variables
OUTPUT_DIR = "./outputs/train/lego_wheel"
JOB_NAME = "lego_wheel_training"
