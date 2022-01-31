#Берегись метеорита
#Игорок должен уворачиваться от падающих метеоритов
from superwires import games, color
import random
games.init(screen_width = 640, screen_height = 480, fps = 50)

class Meteor(games.Sprite):
    """Метеорит"""
    image = games.load_image("1.png")
    speed = 9.8
    def __init__(self, x):
        super(Meteor, self).__init__(image = Meteor.image,
                                     x = x,
                                     y = 10,
                                     dy = Meteor.speed)
    def update(self):
        if self.bottom > games.screen.height:
            self.destroy()
class God(games.Sprite):
    speed = 10
    image = games.load_image("1.png")
    def __init__(self, y = -50, odds_change = 100):
        super(God, self).__init__(image = God.image,
                                  x = games.screen.width/2,
                                  y=y,
                                  dx = God.speed)
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
            new_meteor = Meteor(x=self.x)
            games.screen.add(new_meteor)
            self.time_til_drop = 40
            
   
        
class Survivor(games.Sprite):
    """Марио"""
    image = games.load_image("2.png")
    def __init__(self):
        super(Survivor, self).__init__(image = Survivor.image,
                                       x = games.mouse.x,
                                       bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 30, color = color.black,
                                top = 5, right = games.screen.width -10)
        games.screen.add(self.score)
    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_death()
        self.increase()

    def increase(self):
        Meteor.speed += 0.003
        self.score.value += 1
        self.score.right = games.screen.width - 10
    def check_death(self):
        for met in self.overlapping_sprites:
            self.destroy()
            self.end_game()
        
        

    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 3*games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

def main():
    wall_image = games.load_image("3.jpg", transparent = False)
    games.screen.background = wall_image
    mario = Survivor()
    games.screen.add(mario)
    god = God()
    games.screen.add(god)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()


        
