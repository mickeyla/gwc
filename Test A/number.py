from random import*

#Welcome Message
welcome = "Hello! Welcome to Guess the Number"
print(welcome)

aRandomNumber = randint(1, 20)
i = int(input("Guess a number between 1-20: "))
usertries = 0
while True:
    usertries += 1
    if(usertries >= 4):
        print("WAIT! Game Over.")
        break


    if i < aRandomNumber:
        print("Try a higher number.")
    elif i > aRandomNumber:
        print("Try a lower number.")
    else:
        print("Good Job! You guessed correctly!")
        break

    i = int(input("Guess a number between 1-20: "))
