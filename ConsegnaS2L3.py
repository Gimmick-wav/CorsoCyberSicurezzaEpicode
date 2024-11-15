import random

def yes_no_question(qstn):
    while True:
        nswr=input(qstn).strip().lower()
        if nswr=="y" or nswr=="n":
            return nswr
        else:
            print("\nPlease, enter 'y' or 'n'\n\n ")
rspns=yes_no_question("Welcome to the BandNamesGenerator-O-Matic 3000\n Would you like to generate a unique, never seen before name four your band?\n\n y/n: ")
if rspns=="n":
    print("Oh.. okay:()")
else:
    città=input("First, tell me the name of your hometown: ")
    animale=input("\nThen, tell me the numbers on your credit card ;) haha, jk\n Tell me the name of your pet: ")
    Città=(città).capitalize()
    Animale=(animale).title()
    bndnm=Città +"'s" + " " + Animale+"s"
    print(f"\nComputing...\n Computing...\n  Copmutnig...\n \n\nI could only think of:{bndnm}")
    def yes_no_question2(qstn2):
        while True:
         nswr2=input(qstn2).strip().lower()
         if nswr2=="y" or nswr2=="n":
           return nswr2
        else:
            print("\nPlease, enter 'y' or 'n'\n\n ")
rspns2=yes_no_question("\nWould you like me to think harder? (y/n): ")
if rspns2=="n":
    print("\nHehe I knew I did a good Job")
    exit()
else :
    angrm=Città[:1]+"."+Animale[:1]+"."
    mix=Città[:3]+"-"+animale[:3]
    misto=list(città+animale)
    random.shuffle(misto)
    misto_result=''.join(misto)
    print(f"\n \n What about these?\n{angrm}\n{mix}\n{misto_result}")
while True:
            y=input("\nAre you satisfied now?\n (y/n) ")
            if y == "y":
                print("Kay Byeeee")
                break
            else:
                print("\nThink again, or else :))")