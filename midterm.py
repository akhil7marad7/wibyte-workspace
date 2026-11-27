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
                print("You recruited a", recruit)
            else:
                print("You need more money!")
        else:print("That instrument is unavailable.")
    elif choice=="2":
        if len(band)>0:
            if money>=50:
                money=money-50
                skill=skill+1
                print("Your band's skill increased by 1, which will help you gain money and fans!")
            else:
                print("You need $50 to practice.")
        else:
            print("You need at least one musician to practice!")
    elif choice=="3":
        if len(band)>0:
            if money>=100:
                money=money-100
                concerts=concerts+1
                earnings=(skill+100)+(len(band)*50)
                earnings=earnings+ random.randint(0,100)

                new_fans=skill*len(band)
                new_fans=new_fans+random.randint(1,10)

                money=money+earnings
                fans=fans+new_fans

                print("Your concert was a success!")
                print("You earned $", earnings)
                print("You gained", new_fans, "fans!")
            else:
                print("You need at least $100 to perform at a concert.")
        else:
            print("You need a musician to have a concert!")
    elif choice=="4":
        print("Your Band:")
        print("Your first three musicians are:", band[:3])

        if len(band)>0:
            for musician in band:
                print("-",musician)
        else:
            print("Your band is currently empty.")
    elif choice=="5":
        playing=False
        print("Thanks for playing Build a Band!")
    else:
        print("Invalid choice. Please select a number 1-5.")
    if money<=0:
        playing=False
        print("Your band is bankrupt!")
final_score=money+(fans*2)+(concerts*100)

print("Final Results:")
print("Final money: $", money)
print("Total fans", fans)
print("Concerts completed:", concerts)
print("Final score:", final_score)

if fans>=100:
    print("You became a music superstar!")
elif fans>=25:
    print("Your band is locally known!")
else:
    print("Your band was a fail!")