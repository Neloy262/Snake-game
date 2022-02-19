from snake_env import SnakeEnv
from stable_baselines3 import DQN

env = SnakeEnv()

model = DQN("CnnPolicy", env, verbose=1,buffer_size=100000)
model.learn(total_timesteps=10000, log_interval=4)
model.save("vanilla_dqn_snake")


obs = env.reset()
while True:
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    # env.render()
    if done:
      obs = env.reset()