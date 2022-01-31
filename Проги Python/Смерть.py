class Player (object):
    """Игрок"""
    def blast(self, enemy):
        print("Игрок стреляет в врага.")
        enemy.die()

class Alien (object):
    """Пришелец"""
    def die(self):
        print("Пришелец умер!")

print("Гибель пришельца")
hero = Player()
invader = Alien()
hero.blast(invader)
input("\n\nНажмите Enter, чтобы выйти")
