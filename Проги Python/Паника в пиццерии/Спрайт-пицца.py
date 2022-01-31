#спрайт-пицца
#демонстрирует создание спрайта
from superwires import games
games.init(screen_width = 640, screen_height = 480, fps = 50)
wall_image = games.load_image("1.2.jpg", transparent = False)
games.screen.background = wall_image
pizza_image = games.load_image("4.2.png")
pizza = games.Sprite(image = pizza_image, x = 320, y = 240)
games.screen.add(pizza)
games.screen.mainloop()
