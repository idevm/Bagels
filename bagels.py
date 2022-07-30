import random

NUM_DIGITS: int = 3
MAX_GUESSES: int = 10

def main():
    print(f"""Бейглз, дедуктивная логическая игра

    Я загадываю {NUM_DIGITS}-значное число с неповторяющимися цифрами.
    Попробуй угадать его с такими подсказками:
    - Pico - одна цифра угадана верно, но не на своем месте
    - Fermi - одна цифра угада верно и она на своем месте
    - Bagels - нет такой цифры""")

    while True:
        secretNum: str = getSecretNum()
        print("Я загадал число")
        numGuesses: int = 1
        while numGuesses <= MAX_GUESSES:
            guess: str = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Попытка {numGuesses}: ")
                guess = input("> ")
            clues: str = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print("Закончились попытки")
                print(f"Было загадано число {secretNum}")
                break
        print("Хотите сыграть еще? (да или нет)")
        if not input("> ").lower().startswith("д"):
            break
    print("Спасибо за игру!")

def getSecretNum() -> str:
    numbers: list[str] = list("012345689")
    random.shuffle(numbers)
    secretNum: str = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum) -> str:
    if guess == secretNum:
        return "Угадал!"
    clues: list[str] = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)

if __name__ == "__main__":
    main()