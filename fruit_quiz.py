import random

class Fruit_Quiz:
    def __init__(self):
        self.fruits = {'apple':'red',
                       'orange':'orange',
                       'watermelon':'green',
                       'banana':'yellow'}
    def quiz(self):
        while True:
            fruit, colour = random.choice(list(self.fruits.items()))

            print("What is the colour of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower() == colour):
                print("CORRECT ANSWER")
            else:
                print("WRONG ANSWER")
            
            option = int(input("Enter 0 if you want to play again, otherwise Enter 1"))

print("Welcome to Fruit Quiz")
fq = Fruit_Quiz()
fq.quiz()