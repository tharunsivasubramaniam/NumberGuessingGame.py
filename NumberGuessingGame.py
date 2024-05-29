import random

print("Welcome to Number Guessing Game")
print("Are You Ready to Play With Me...Okay Let's Start The Game")
try:
    e = ''
    while e != 'c':
        print("Enter the number range that you are going to guess (EX:1,10)")
        st, ed = map(int, input().split(","))
        rm = random.randint(st, ed)
        ct = ""
        chance = 0
        while ct != "okay":
            gs = int(input("Guess the Number...."))
            chance += 1
            if st <= gs <= ed:
                if gs == rm:
                    print("\nWOW...!Your Guess Is Correct Brilliant")
                    print("You Have Won Me in", end=" ")
                    if chance == 1:
                        print("1st Chance")
                        print("Nega Vera Level...Ungaluku Bright Future Iruku")
                    elif chance == 2:
                        print("2nd Chance")
                        print("Nega Enga Ponalu Polachupiga")
                    elif chance == 3:
                        print("3rd Chance")
                        print("Paravala Unagaluku Konjo Mula Iruku")
                    else:
                        print(str(chance) + "th Chance")
                    ct = "okay"
                elif gs > rm:
                    print("Sorry Your Guess is too high")
                    print("One More Chance", end=" ")

                else:
                    print("Sorry Your Guess is too low")
                    print("One More Chance", end=" ")

            else:
                print("Useless...Sorry Guess The Number Between " + str(st) + " And " + str(ed))
                print("\n")
        print("_____Are you like to play again press any letter rather than C____")
        e = input("If you like to close press C : ")
        if e == 'C':
            e = 'c'

except ValueError:
    print("Something went wrong!")
    print("Please check the values you entered and try again")
