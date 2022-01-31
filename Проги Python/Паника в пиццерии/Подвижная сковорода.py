#Подвижная сковорода
#Демонстрирует ввод с помощью мыши
from superwires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)
class Pan(games.Sprite):
    """Перемещаемая мышью сковорода"""
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
def main():
    wall_image = games.load_image("1.2.jpg", transparent = False)
    games.screen.background = wall_image
    pan_image = games.load_image("5.png")
    the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
main()
