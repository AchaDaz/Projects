#Гибель пришельца
#Демонстрирует взаимодействие объектов
class Player(object):
    """Игрок в экшн-игре"""
    def blast(self,enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()

class Alien(object):
    """Враждебный пришелец в экшн-игре"""
    def die(self):
        print("\nПришелец помер:(")

print("\t\tГибель пришельца\n")
hero = Player()
invader = Alien()
hero.blast(invader)
input("\n\nНажмите Enter, чтобы выйти...")
