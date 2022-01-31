#Паника в пиццерии
#Игрок должен ловить падающую пиццу, пока она не достигла земли
from superwires import games, color
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)
class Pan(games.Sprite):
    """Сковорода"""
    image = games.load_image("5.png")
    def __init__(self):
        super(Pan, self).__init__(image = Pan.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 25, color = color.black,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pizza.handle_caught()
            if self.score.value % 100 == 0:
                Pizza.speed += 0.1
                Chef.speed += 0.1
            if self.score.value == 500:
                add()
                
                                               
class Pizza(games.Sprite):
    """Пицца"""
    image = games.load_image("4.2.png")
    speed = 1
    def __init__(self, x, y = 115):
        super(Pizza, self).__init__(image = Pizza.image,
                                    x=x, y=y,
                                    dy = Pizza.speed)
    def update(self):
        """Проверяет на наличие падения"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
    def handle_caught(self):
        self.destroy()
    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 2*games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

class Chef(games.Sprite):
    image = games.load_image("6.png")
    speed = 3
    def __init__(self, y = 79, odds_change = 100):
        super(Chef, self).__init__(image = Chef.image,
                                   x = games.screen.width/2,
                                   y = y,
                                   dx = Chef.speed)
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update (self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = - self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = - self.dx
        self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x=self.x)
            games.screen.add(new_pizza)
            self.time_til_drop = int(new_pizza.height * 1.3/Pizza.speed) + 2
        
        
def add():
    the_chef2 = Chef()
    games.screen.add(the_chef2)

def main():
    wall_image = games.load_image("1.2.jpg", transparent = False)
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan()
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()
            
