#Фоновая картинка
#Демонстрирует назначение картинки для графического экрана
from superwires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)
wall_image = games.load_image("1.jpg", transparent = False)
games.screen.background = wall_image
games.screen.mainloop()
