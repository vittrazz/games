import random
print("Добро пожаловать в числовую угадайку")
print("В каком диапазоне загадать число? от 1 до ...")
n = int(input())
num = random.randint(1, n)
def is_valid(a):
    return a.isdigit() and 100 >= int(a) >= 1
count = 0
while True:
    num_user = input("Введите число, которое загадал комп: ")
    if is_valid(num_user) == True:
        if int(num_user) > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
            count += 1
        elif int(num_user) < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            count += 1
        else:
            print("Вы угадали, поздравляем!")
            count += 1
            print(f'Количество попыток: {count}. Попробуете еще раз? Да/Нет')
            count = 0
            answer = input().lower()
            if answer == 'да' or answer == 'lf':
                print("В каком диапазоне загадать число? от 1 до ...")
                n = int(input())
                num = random.randint(1, n)
                continue
            else:
                print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                break
        
    else:
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue