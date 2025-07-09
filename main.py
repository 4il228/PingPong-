#подключение библиотеки
from pygame import *

#создание окна игры
win = display.set_mode((700,500))
display.set_caption('PingPong')


game = True

clock = time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)#发士大夫鬼地方如果和