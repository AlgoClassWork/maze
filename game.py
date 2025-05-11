from pygame import *
#Класс для персонажей игры
class GameSprite(sprite.Sprite):
    def __init__(self, img, width, height, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    #Функция для отображения персонажей
    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

    #Функция для передвижения с помощью клавиатуры
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 600:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = Surface( (width, height) )
        self.image.fill( (0, 100, 0) )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )

#Создание стен
wall_1 = Wall(10, 350, 150, 150)
wall_2 = Wall(400, 10, 150, 150)
wall_3 = Wall(400, 10, 300, 300)
#Создание персонажей
hero = GameSprite('hero.png', 80, 80, 0, 400, 3)
enemy = GameSprite('enemy.png', 80, 80, 600, 300, 1)
goal = GameSprite('goal.png', 80, 80, 600, 400, 0)
#Создание экрана
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
window = display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
display.set_caption('Лабиринт')
# Загрузка изображений
BACKGROUND = transform.scale(image.load('background.jpg') , (WINDOW_WIDTH, WINDOW_HEIGHT))
# Добавление музыки на задний фон
#mixer.init()
#mixer.music.load('music.mp3')
#mixer.music.play()
#Игровой цикл
while True:
    # Обработка выхода из игры 
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
    # Отображение заднего фона
    window.blit( BACKGROUND , (0, 0) )
    # Отображение персонажей
    hero.show()
    enemy.show()
    goal.show()
    # Отображение стен
    wall_1.show()
    wall_2.show()
    wall_3.show()
    # Движение персонажей
    hero.move()
    # Обновление кадров
    display.update()
