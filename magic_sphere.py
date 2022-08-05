from random import *
from time import sleep

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

print("Hello! Print your question for me to answer.")

answeres = ['Yes, goddamnit', "It's already defined. ", 'Without any doubts.', 'Actually you are right.', 'Foreordained',
            'Yes', 'Propably, i think', 'Most likely', 'Icons say - yes.', 'Good prospects.',
            "I didn't understand. Try again", 'Ask me later...', 'You better not to know that))', "It's impossible to predict now", 'Concentrate and ask me again.',
            "Don't even think.", "My answer's NO, and i'm sure in it's certainty.", 'According to my infarmation - No.', "The prospects are not that good.", 'Highly doubtful.' ]
while True:
    question = str(input('Your question: '))
    predict = randint(1, 19)
    print("Well, well, well... My answer iiisss...")
    sleep(3)
    print(answeres[predict])
    if predict >= 15:
        sleeping()
        print("So, that just happened")
    sleep(3)
    continueing = input("Do you want to find out your future again? (Yes = 'y', No = 'n')\n" )
    if fool_defend(continueing) == 'n':
        print("Hey, pay me your 60 buxes before you go!")
        sleeping()
        break
    else:
        print("Good. Let's start again")
        sleeping()
        continue 