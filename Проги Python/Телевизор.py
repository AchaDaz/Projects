#Программа Телевизор
#Имитирует работу телевизора
class Tv(object):
    """Телевизор"""
    def __init__(self, volume=0, channel=1):
        self.volume = volume
        self.channel = channel

    @property
    def channel_change(self):
        return self.channel

    @property
    def volume_change(self):
        return self.volume
    
    @channel_change.setter
    def channel_change (self, new_channel):
        if 1<=new_channel<=100:
            self.channel = new_channel
            print("\nКанал успешно переключен!")
        else:
            print("\nНет возможности переключиться на этот канал!")

    @volume_change.setter
    def volume_change(self, new_volume):
        if 0<=new_volume<=20:
            self.volume = new_volume
            print("\nГромкость успешно изменена!")
        else:
            print("\nНет возможности выставить такую громкость!")

#Основное тело
def main():
    TV1 = Tv()
    choice = None
    while choice != "0":
        print \
        ("""
        Телевизор
        0 - Выключить телевизор
        1 - Изменить канал
        2 - Изменить громкость
        """)
        choice = input("Ваш выбор:")
        print()

        if choice == "0":
            print("Телевизор выключен.")
        elif choice == "1":
            TV1.channel_change = int(input("Введите номер канала: "))
        elif choice == "2":
            TV1.volume_change = int(input("Введите новую громкость: "))
        elif choice == "3":
            print(TV1.channel)
            print(TV1.volume)
        else:
            print("\nА такую команду еще не изобрели!")


main()

input("\n\nНажмите Enter, чтобы выйти")
        
