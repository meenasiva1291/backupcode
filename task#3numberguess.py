import random

#initial print
print("Welcome to number guess game")

#initialize range value
lower = int(input("Enter the lower range value:"))
upper = int(input("Enter the upper range value:"))

#print statement
print("You have 5 guess to find a number")

#intialize the variable
number= random.randint(lower,upper)
ch = 5
gu = 0

while gu < ch:
    gu  += 1
    guess = int(input('Enter the guess:'))

    if number == guess:
        print(f'congratulations, your guess is right and the number is {guess}.you guess it in {gu} attempts')
        break
    elif gu >= ch and number!=guess:
        print(f'you lose the game and the correct number is {number}')
    elif guess>number:
        print("your guess is high")
    elif guess<number:
        print("Your guess is low")