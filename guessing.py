import random
print("Number Guessing Game")

number = random.randint(1,9)
chances = 0
print("Guess the number(Between 1 to 9)")

while chances < 5:
    guess = int(input("Enter your Guess : "))

    if guess == number:
        print("Congratulation , You WON !!!")

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else :
        print("Your guess was too high, guess lower than",guess)

chances += 1

if not chances < 5 :
    print("You LOST!!! ,the number is",number)

