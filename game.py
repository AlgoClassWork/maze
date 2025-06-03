from pygame import *

class GameSprite(sprite.Sprite):
    # Свойства наших персонажей
    def __init__(self, img, cord_x, cord_y, width, height):
        self.image = transform.scale( image.load(img), (width, height) )
        self.rect = self.image.get_rect()
        self.rect.x = cord_x
        self.rect.y = cord_y
    # Способность отображатся
    def show(self):
        window.blit( self.image, (self.rect.x, self.rect.y) )
    # Способность передвигаться
    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 1
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += 1
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= 1
        if keys[K_d] and self.rect.x < 620:
            self.rect.x += 1

    def auto_move(self):
        if self.rect.x <= 300:
            self.side = 'right'
        if self.rect.x >= 600:
            self.side = 'left'
        
        if self.side == 'left':
            self.rect.x -= 1
        else:
            self.rect.x += 1

# Создание персонажей
hero = GameSprite(img='hero.png', cord_x=0, cord_y=400, width=80, height=100)
enemy = GameSprite(img='enemy.png', cord_x=600, cord_y=200, width=100, height=80)
goal = GameSprite(img='goal.png', cord_x=600, cord_y=420, width=100, height=80)

wall_1 = GameSprite(img='wall.png', cord_x=150, cord_y=150, width=10, height=400)
wall_2 = GameSprite(img='wall.png', cord_x=150, cord_y=150, width=400, height=10)

# Создание экрана
window = display.set_mode( (700, 500) )

clock = time.Clock()

# Игровой цикл
while True:
    # Обработка нажатия на крестик (выход из игры)
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    # Заливка фона определенным цветом
    window.fill( (150, 150, 250) )

    # Отображение персонажей
    hero.show()
    enemy.show()
    goal.show()

    wall_1.show()
    wall_2.show()

    # Движение персонажей
    hero.move()
    enemy.auto_move()

    # Постоянное обновление кадров на нашем экране
    display.update()
    clock.tick(100)
