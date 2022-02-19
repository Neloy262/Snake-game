import pygame
import random
from preprocess_image import process
pygame.init()

WIN_HEIGHT = 500
WIN_WIDTH = 900
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 30
L = []
SNAKE_SIZE = 15

surface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf",20)
textx = 10
texty = 10
score = 0

class Food():

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.head = pygame.rect.Rect(self.x,self.y,SNAKE_SIZE,SNAKE_SIZE)
    def draw(self):
         pygame.draw.rect(surface, (255,0,255), self.head)

class Snake():

    def __init__(self,x,y):
        self.body = []
        self.head = pygame.rect.Rect(x,y,SNAKE_SIZE,SNAKE_SIZE)
        self.body.append(self.head)
        self.eaten = False
        self.points = 0
    

    def draw_body(self,surface):
        val = 0
        for i,b in enumerate(self.body):
            pygame.draw.rect(surface, BLACK, self.body[i])


    def increase(self):
        self.points+=1
        self.body.append(pygame.rect.Rect(self.body[-1].x,self.body[-1].y,SNAKE_SIZE,SNAKE_SIZE))
    
    def move(self,val):
        if val == 0:
                        
            for i,b in enumerate(self.body):
                if i==0:
                    prev = self.body[i].copy()
                    self.body[0].move_ip(SNAKE_SIZE,0)
                    continue

                temp = self.body[i].copy()
                self.body[i] = prev.copy()
                prev = temp.copy()

                  
        if val == 1:
            

            for i,b in enumerate(self.body):
                if i==0:
                    prev = self.body[i].copy()
                    self.body[0].move_ip(-SNAKE_SIZE,0)
                    continue
                temp = self.body[i].copy()
                self.body[i] = prev.copy()
                prev = temp.copy()

        if val == 2:
            
            for i,b in enumerate(self.body):
                if i==0:
                    prev = self.body[i].copy()
                    self.body[0].move_ip(0,-SNAKE_SIZE)
                    continue
                temp = self.body[i].copy()
                self.body[i] = prev.copy()
                prev = temp.copy()

        if val == 3:
            

            for i,b in enumerate(self.body):
                if i==0:
                    prev = self.body[i].copy()
                    self.body[0].move_ip(0,SNAKE_SIZE)
                    continue
                temp = self.body[i].copy()
                self.body[i] = prev.copy()
                prev = temp.copy()


        if val == 4:
            return

    
        
            
def Eat(rect1,rect2):

    return rect1.colliderect(rect2)

def gameover(snake):

    if snake.body[0].x >= 900 or snake.body[0].x < 0:
        return -1

    if snake.body[0].y >= 500 or snake.body[0].y < 0:
        return -1
    

    val = snake.body[0].collidelist(snake.body[1:])
    val2 = snake.body[0].y

    for i in snake.body:
        if val2!=i.y:
            if val!=-1:
                return -1
    

    return 1
    
def show_score():
    global score
    score_font = font.render("Score:"+str(score),True,(0,0,0))
    surface.blit(score_font,(textx,texty))

def main():
   
    
    snake = Snake(300,250)
    fx = random.randint(10,890)
    fy = random.randint(10,490)
    food = Food(fx,fy)
    eaten = False
    run = True
    val = -1
    # surface.fill((255,255,255))
    while run:
    
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    val=1
                if event.key == pygame.K_RIGHT:
                    val=0

                if event.key == pygame.K_UP:
                    val=2

                if event.key == pygame.K_DOWN:
                    val=3
        
        surface.fill((255,255,255))
        snake.draw_body(surface)
        food.draw()
        snake.move(val)
       
        if eaten:
            global score
            score+=1
            snake.increase()
            fx = random.randint(10,890)
            fy = random.randint(10,490)
            food = Food(fx,fy)
        
        
        
        clock.tick(FPS)
        
        eaten=Eat(snake.body[0],food.head)
        
        gm = gameover(snake)
        show_score()
        pygame.display.update()
        if gm==-1:
            break
        
        


    pygame.quit()


if __name__=="__main__":
    main()



