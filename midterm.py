import random

#beginning stats
money=500
fans=0
skill=1
concerts=0
band=[]

#available instruments

available_instruments=[ 
    "Piano",
    "Guitar",
    "Trumpet",
    "Bass",
    "Drums",
    "Singer",
]

print("Welcome to Build A Band!")
print("The objective of this game is to build your band and become famous!")

playing=True

while playing==True:

    print("Current Stats")

    print("Money: $", money)

    print("Fans:", fans)

    print("Skill:", skill)

    print("Concerts played:", concerts)

    print("1. Recruit a musician")

    print("2. Practice")

    print("3. Play a concert")

    print ("4. View band")

    print("5. Quit")

    choice=input("Choose an action (1-5): ")

    if choice=="1": 
        for instruments in available_instruments:
            print(instruments)
        recruit=input("Which instrument do you want?")

        recruit=recruit.title()

        if recruit in available_instruments:
            if money>=150:
                money=money-150
                band.append(recruit)
                available_instruments.remove(recruit)
                print("You recruited a", recruit +"player!")
            else:
                print("You need more money!")
        else:print("That instrument is unavailable.")
    elif choice=="2":

