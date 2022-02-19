from cgitb import reset
from gym import Env
from gym.spaces import Box,Discrete
import numpy as np
import random
import pygame
from snake import Snake,Food,gameover,Eat
from preprocess_image import process
from stable_baselines3.common.env_checker import check_env

WIN_HEIGHT = 500
WIN_WIDTH = 900
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 30
SNAKE_SIZE = 15
clock = pygame.time.Clock()

class SnakeEnv(Env):

    def __init__(self):
        super(SnakeEnv, self).__init__()
        self.action_space = Discrete(5)
        self.observation_space = Box(low=0, high=255,shape=(84, 84,1), dtype=np.uint8)
        self.surface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.snake = Snake(300,250)
        fx = random.randint(20,880)
        fy = random.randint(20,480)
        self.food = Food(fx,fy)



    def step(self,action):
       
        frames = []
        reward = 1
        prev_point = self.snake.points
        info_dict = {"info":""}
        for i in range(2):
            self.snake.move(action)
            self.render()

            if gameover(self.snake) == -1:
                # print("GAMEOVER")
                return np.zeros((84, 84, 1)), -1000 , True, info_dict

            frames.append(process(pygame.surfarray.array3d(self.surface)))

        eaten = Eat(self.snake.body[0],self.food.head)

        if eaten:
            # print("EATEN")
            self.snake.increase()
            fx = random.randint(10,890)
            fy = random.randint(10,490)
            self.food = Food(fx,fy)
            reward = 1000

        # pygame.display.update()
        return frames[1] - frames[0] ,reward,False, info_dict 

    def reset(self):
        self.snake = Snake(300,250)
        fx = random.randint(20,880)
        fy = random.randint(20,480)
        self.food = Food(fx,fy)

        self.render()

        
        return process(pygame.surfarray.array3d(self.surface))
        

    def render(self):
        self.surface.fill((255,255,255))
        self.food.draw()
        self.snake.draw_body(self.surface)
        pygame.display.update()



env = SnakeEnv()
check_env(env)
