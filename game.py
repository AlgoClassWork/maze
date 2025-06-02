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

# Создание персонажей
hero = GameSprite(img='hero.png', cord_x=0, cord_y=400, width=80, height=100)
enemy = GameSprite(img='enemy.png', cord_x=600, cord_y=200, width=100, height=80)
goal = GameSprite(img='goal.png', cord_x=600, cord_y=420, width=100, height=80)

wall_1 = GameSprite(img='wall.png', cord_x=150, cord_y=150, width=10, height=400)
wall_2 = GameSprite(img='wall.png', cord_x=150, cord_y=150, width=400, height=10)

# Создание экрана
window = display.set_mode( (700, 500) )

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
    # Постоянное обновление кадров на нашем экране
    display.update()
