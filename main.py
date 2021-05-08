# ================== Start ==================
import pygame
import random


# ================== Class ==================
class Snake:
    def __init__(self):
        self.w = 16
        self.h = 15
        self.x = width / 2
        self.y = height / 2
        self.color = (9, 59, 27)
        self.speed = 5
        self.score = 1
        self.x_change = 0
        self.y_change = 0
        self.body = []
        self.colorBody = (214, 103, 88)
        self.length = 0

    def show(self):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.w, self.h])
        # pygame.draw.ellipse(window, self.color, [self.x, self.y, self.w, self.h])
        for parts in self.body:
            pygame.draw.ellipse(window, self.colorBody, [parts[0], parts[1], self.w, self.h])

        if len(self.body) > self.length:
            self.body.pop(0)

    def move(self):
        self.body.append([self.x, self.y])
        if self.x_change == -1:
            self.x -= self.speed
        elif self.x_change == 1:
            self.x += self.speed
        elif self.y_change == -1:
            self.y -= self.speed
        elif self.y_change == 1:
            self.y += self.speed

    def apple_eat(self):
        if apple.x - apple.r <= self.x <= apple.x + apple.r and apple.y - apple.r <= self.y <= apple.y + apple.r:
            self.score += 1
            self.length += 1
            snake.speed += 0.5
            return True
        else:
            return False

    def pear_eat(self):
        if pear.x - pear.r <= self.x <= pear.x + pear.r and pear.y - pear.r <= self.y <= pear.y + pear.r:
            self.score += 2
            self.length += 2
            snake.speed += 0.5
            return True
        else:
            return False

    def min_eat(self):
        if min.x - min.r <= self.x <= min.x + min.r and min.y - min.r <= self.y <= min.y + min.r:
            self.score -= 1
            self.length -= 1
            snake.speed -= 0.5
            return True
        else:
            return False


class Apple:
    def __init__(self):
        self.r = 27
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.image = pygame.image.load("pic/apple.png")
        self.bg2 = pygame.transform.scale(self.image, (27, 27))

    def show(self):
        window.blit(self.bg2, [self.x, self.y])


class Pear:
    def __init__(self):
        self.r = 30
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.image = pygame.image.load("pic/pear.png")
        self.bg2 = pygame.transform.scale(self.image, (self.r, self.r))

    def show(self):
        window.blit(self.bg2, [self.x, self.y])


class Min:
    def __init__(self):
        self.r = 35
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.image = pygame.image.load("pic/min.png")
        self.bg2 = pygame.transform.scale(self.image, (self.r, self.r))

    def show(self):
        window.blit(self.bg2, [self.x, self.y])


if __name__ == '__main__':
    # ================== Settings ==================
    pygame.init()
    width = 600
    height = 400
    icon = pygame.image.load("pic/icon.jpg")
    bg = pygame.image.load("pic/bg.jpg")
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sadegh Game")
    pygame.display.set_icon(icon)
    bg2 = pygame.transform.scale(bg, (width, height))
    font = pygame.font.Font(None, 30)
    clock = pygame.time.Clock()
    # ================== Variables ==================
    snake = Snake()
    apple = Apple()
    pear = Pear()
    min = Min()

    while True:
        # ================== Events ==================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.x_change = -1
                    snake.y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.x_change = 1
                    snake.y_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.y_change = -1
                    snake.x_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.y_change = 1
                    snake.x_change = 0
        window.blit(bg2, (0, 0))
        # ================== Wall ==================
        # if snake.x < 0:
        #     snake.x = height
        # elif snake.x > height:
        #     snake.x = 0
        # elif snake.y < 0:
        #     snake.y = width
        # elif snake.y > width:
        #     snake.y = 0
        if snake.x > width - snake.w or snake.x < 0 or snake.y > height - snake.h or snake.y < 0:
            pygame.quit()
            quit()
        # ================== Move and Show ==================
        snake.move()
        snake.show()
        apple.show()
        pear.show()
        min.show()
        # ================== If ==================
        snake.apple_eat()
        if snake.apple_eat():
            apple = Apple()

        snake.pear_eat()
        if snake.pear_eat():
            pear = Pear()

        snake.min_eat()
        if snake.min_eat():
            min = Min()

        if snake.score % 5 == 0:
            text = font.render(f"VeryGood", True, (14, 204, 6))
            window.blit(text, (470, 20))

        if snake.score == 0 or snake.score < 0:
            text = font.render(f"BeCareful", True, (255, 0, 0), (0, 0, 0))
            window.blit(text, (470, 20))

        text = font.render(f"Score: {snake.score}", True, (87, 204, 217))
        window.blit(text, (15, 15))
        # ================== End ==================
        pygame.display.update()
        clock.tick(30)
