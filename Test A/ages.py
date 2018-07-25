import json

redo=1
listofdict=[]

#json stuff
#open() opens a file
#write() erases everything in the file
"""
story = open("ages.txt", "r")
for line in story:
    list.append(line)
story.close()

story = open("ages.txt", "w")
for line in story:
    list.append(line)
    list.append("hey")
"""

"""
*** PRINTS "ONCE UPON A TIME" (it was in the json file)
or
    list.append(line)
    print(list)
*** PRINTS THE STUFF AS A LIST

"""
''
while redo==1:
    answerlist = {}
    name = input("What is your name?")
    answerlist["Name"] = name

    birthday = input("What month were you born?")
    answerlist["Birthday"] = birthday

    animal = input("What animal do you just, hate?")
    answerlist["Animal"] = animal

    objects = input("What inanimate object do you wish you could eliminate from existence??")
    answerlist["Objects"] = objects

    fear = input("What do you fear?")
    answerlist["Fear"] = fear

    state = input("What state will you never go to?")
    answerlist["State"] = state

    color = input("What color is most offensive?")
    answerlist["Color"] = color

    food = input("What food do you hate most??")
    answerlist["Food"] = food

    listofdict.append(answerlist)

    question= input("Is there another person? Y/N?")
    if question == "Y":
        print(answerlist)
        continue
    else:
        print(answerlist)
        break

print(listofdict)
f= open("ages.json","r")
olddata = 0
olddata = json.load(f)
listofdict.extend(olddata)
f.close()
# responses = open("ages.json", "r")

answers = open("ages.json","w")
answers.write('[')
for i in range(len(listofdict) - 1):

    # answers.write(str(i)\n)

    json.dump(listofdict[i], answers)
    answers.write(",\n")


json.dump(listofdict[len(listofdict) - 1], answers)
answers.write("]")
answers.close()
