from snake_env import SnakeEnv
from stable_baselines3 import DQN

env = SnakeEnv()

model = DQN("CnnPolicy", env, verbose=1,buffer_size=100000)
model.learn(total_timesteps=1, log_interval=4)
