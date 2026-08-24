import random

jackport = random.randint(1,100)

guess = int(input("guess the number"))
count = 1

while guess != jackport:
    if guess < jackport:
        print("guess higher numbwe")
    else:
        print("guess lower number")

    guess = int(input("guess the number"))
    count += 1

    print("correct answer")
    print("you took",count,"attempts")
