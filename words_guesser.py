from random import *

random_number = randrange(1, 100)

print("Вгадай число від 1 до 100. ")
count = 1

while True:
    your_try = int(input())
    if your_try > random_number:
        print("Це занадто, брате. Спробуй трохи менше")
        count += 1
        continue
    elif your_try < random_number:
        print("Ну, якось невпевнено вийшло. Більше треба. ")
        count += 1
        continue
    else:
        print("Да ти геній! Нічого собі. Зайняло лише якісь", count, "спроб!")
        break

# tries counter with fool_defend

# def is_num(n):
#     return n.isdigit()
    
# n = input()

# while True:
#     if is_num(n) == False:
#         print("not an int, try again")
#         n = input()
#     else:
#         print(ceil(log2(int(n))))
#         break