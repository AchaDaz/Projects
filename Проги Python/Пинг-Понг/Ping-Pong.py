#Игра пинг-понг
from superwires import games, color
import random
games.init(screen_width = 800, screen_height = 600, fps = 50)
class Skate(games.Sprite):
    """Ракетка в виде скейта"""
    image = games.load_image("1.png")
    def __init__(self):
        super(Skate, self).__init__(image = Skate.image,
                                    x = games.mouse.x,
                                    bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 20, color = color.black,
                                top = 6, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_contact()

    def check_contact(self):
        for ball in self.overlapping_sprites:
            ball.change_way()
            self.score.value += 1
            self.score.right = games.screen.width - 10

class Ball(games.Sprite):
    image = games.load_image("2.png")
    speed = 5
    def __init__(self):
        super(Ball, self).__init__(image = Ball.image,
                                    x = random.randrange(800),
                                    y = 50,
                                    dx = Ball.speed,
                                    dy = Ball.speed)
    def update(self):
        if self.right > games.screen.width or self.left < 0 :
            self.dx = - self.dx
        if self.top < 0:
            self.dy = - self.dy
        self.check_lose()

    def change_way(self):
        self.dy = - self.dy
        Ball.speed += 0.2

    def check_lose(self):
        if self.y > games.screen.height:
            self.end_game()
            self.destroy
    def end_game(self):
        end_message = games.Message(value = "Game Over",
                                    size = 100,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 4 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

def main():
    wall_image = games.load_image("3.jpg", transparent = False)
    games.screen.background = wall_image
    ball = Ball()
    skate = Skate()
    games.screen.add(ball)
    games.screen.add(skate)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

main()






    
