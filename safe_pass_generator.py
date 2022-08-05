from random import choice
from time import sleep

def fool_defend_len(s):
    while not s.isdigit() or int(s) < 5 or int(s) > 50:
        if not s.isdigit():
            print("Type DIGIT, please")
            s = input()
            continue
        elif int(s) < 5:
            print("Your input must be >= 5")
            s = input()
        else:
            print('Your input must be <= 50')
            s = input()

    return s

def fool_defend(s):
    continueing = s
    while continueing.lower() != 'n' and continueing.lower() != 'y':
        print('your answer is invalid. Type again, please')
        continueing = input("Yes = 'y', No = 'n'\n" )
    return continueing.lower()

def sleeping():
    for _ in range(3):
        sleep(0.8)
        print('.', end = ' ')
    print()

def array(d, l, u, s):
    chars = []
    whatlen = input("\nWhat lenght of password do you want?\n")
    whatlen = fool_defend_len(whatlen)
    ifdig = input("Do you want digits in your password? (Yes = y, No = n)\n")
    ifdig = fool_defend(ifdig)
    iflow = input("Do you want lowercase letters in your password? (Yes = y, No = n)\n")
    iflow = fool_defend(iflow)
    ifupp = input("Do you want uppercase letters in your password? (Yes = n, No = n)\n")
    ifupp = fool_defend(ifupp)
    ifsym = input("Do you want special symbols in your password? (Yes = y, No = n)\n")
    ifsym = fool_defend(ifsym)
    if ifdig == 'y':
        chars += d
    if iflow == 'y':
        chars += l
    if ifupp == 'Y':
        chars += u
    if ifsym == 'y':
        chars += s
    return chars, int(whatlen)

def generate_password(chars, length):
    while len(chars) == 0:
        print("Hey!", end=' ')
        sleep(1.5)
        print("I don't have elements to work with!")
        sleep(2)
        sleeping()
        chars, length = array(digits, lowercase, uppercase, symbols)
    print("Creating.")
    sleeping()
    print("Here's your password!")
    password = [choice(chars) for _ in range(length)]
    return password

count = 0
digits = [int(i) for i in range(10)]
lowercase = [i for i in 'abcdefghijklmnopqrstuvwxyz']
uppercase = [i for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
symbols = [i for i in '@#$%&!^-+=_']

sleeping()
print("\nWelcome to safe password generator!")

while True:
    chars, length = array(digits, lowercase, uppercase, symbols)
    print(*generate_password(chars, length), sep='')
    continuing = fool_defend(input("Do you want to create another one? (Yes = y, No = n)\n"))
    if continuing == 'y':
        print("Good! Let's start the work!")
        sleeping()
        count += 1
        continue
    else:
        print("Thanks for using our application! It's", count * 50, "buxes from you :)")
        sleeping
        break
