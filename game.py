from pygame import *

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
    
    # Постоянное обновление кадров на нашем экране
    display.update()
