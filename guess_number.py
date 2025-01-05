from random import randint


# Add comment
is_guess = False #
number = randint(1,100)

def main():
    while not is_guess:
        # Ввод числа 
        num_check = int(input('Введите ваше число: '))

        if num_check == number:
            is_guess = True
            break;

        if num_check < number:
            print('Ваше число меньше того, что загадано.') 

        if num_check > number:
            print('Ваше число больше того, что загадано.')               

main()
print('Отличная интуиция! Вы угадали число :)')

