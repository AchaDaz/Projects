# Игра виселица
import random
HANGMAN = (
    """
    ------
    |   |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |   |
    |   O
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |   |
    |   O
    |   |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |   |
    |   O
    |   |
    |   |
    |  |
    |  |
    |
    |
    ----------
    """,
    """
    ------
    |   |
    |   X
    |   |
    |   |
    |  | |
    |  | |
    |
    |
    ----------
    """)
MAX_WRONG = len(HANGMAN) -1
WORDS = ("ТИТАН", "ЛАЗУРИТ", "ХАРТСТОУН", "МАЙНКРАФТ", "ФИЛЬТР")
word = random.choice(WORDS) #слово для отгадывания
so_far = '-'*len(word) #буквы в слове заменили дефисами
wrong = 0 #число ошибок
used = [] #предложенные буквы
print("Добро пожаловать в игру ВИСЕЛИЦА!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже предлагали буквы: \n", used)
    print("\nОтгаданное вами выглядит так: \n", so_far)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже предлагали букву", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nДа, такая буква есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nК сожалению, такой буквы нет.")
        wrong +=1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nВас повесили!")
else:
    print("\nВы отгадали!")
print("\nБыло загадано слово", word)
input("\n\nНажмите Enter, чтобы выйти.")

