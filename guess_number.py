from random import randint


# Add comment
number = randint(1, 100)


def main():
    is_guess = False  # Variable.
    while is_guess is False:
        # Ввод числа
        num_check = int(input('Введите ваше число: '))

        if num_check == number:
            is_guess = True
            break
        elif num_check < number:
            print('Ваше число меньше того, что загадано.')
        elif num_check > number:
            print('Ваше число больше того, что загадано.')


main()
print('Отличная интуиция! Вы угадали число :)')
