import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"""Бейглз, дедуктивная логическая игра
    Я загадываю {NUM_DIGITS}-значное число с неповторяющимися цифрами.
    Попробуй угадать его с такими подсказками:
    - Pico - одна цифра угадана верно, но не на своем месте
    - Fermi - одна цифра угада верно и она на своем месте
    - Bagels - нет такой цифры""")

    while True:
        secret_num = get_secret_num()
        print("Я загадал число")


        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Попытка {num_guesses}: ")
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("Закончились попытки")
                print(f"Было загадано число {secret_num}")
                break
                    
        print("Хотите сыграть еще? (да или нет)")
        if not input("> ").lower().startswith("д"):
            break

    print("Спасибо за игру!")

def get_secret_num():
    numbers = list("012345689")
    random.shuffle(numbers)
    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    if guess == secret_num:
        return "Угадал!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)

if __name__ == "__main__":
    main()