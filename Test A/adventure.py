start = "Hello, YOU are Ruby, a bored teenager in her room. Suddenly, you are transported into a magical forest where she meets Gobo, a goblin. He tells her that she is the chosen one, meant to save the princess from the evil ghoul."
print(start)

first = input("Gobo asks if you will accept the challenge. Will you? (Y/N)")

while True:

    if first == "Y":
        print("Gobo asks that you follow him.")

    if first=='N':
        print('You are transported back to your room. Play again?')
        break

    middle = "You are now on your way to meet The Master Wizard. Gobo tells you that the Master will grant you the power to defeat the ghoul."
    print(middle)

    second = input("The wizard tells you that you need to trust him in order for your powers to work. Do you trust him? (Y/N)")
    if second == "N":
        print("Gobo tells you that you will have to fight without your powers.")
    last1 = "You make your way to the castle where you encounter the ghoul and you lose. The end. Play again?"
    if second == "Y":
        print("You are granted powers and make your way to the castle where you encounter the ghoul. First, he knocks you down but you persist and defeat him and turn him into a squirrel.")

    last = input("The princess is saved! As a token of her gratitude, she asks you to stay and be her protector. Will you accept? (Y/N)")
    if last == "Y":
        print("You stay and become prosperous. Game over!")
    if last == "N":
        print("You return to your room, just as bored as before. Game over!")
        break
