#Imports
import time
from pathlib import Path
import json

#Globals
data = {
    #Areas
    "cell": True,

    #Variables
    "brName": "",
    "name": "",
    "jamesInteract": False,
    "jamesInitiate": False,
    "jamesName": False,
    "jamesKnife": False,
    "inventory": [],
    "pillowInventory": [],
    "pillowUsed": False,
}

#savedata paths
savepath = Path("./savedata.json")
gamepath = Path("./gamedata.json")

def save():
    pass


def load():
    pass


#game start


#game intro
print("What is your name?")
data["brName"] = str(input("> ").capitalize())
time.sleep(2)
print("What is your brothers name?")
data["name"] = str(input("> ")).capitalize()
time.sleep(2)
print()
input("<<PRESS ENTER TO CONTINUE DIALOGUE>>")
print()
input("Five days from now, They strap my brother "+data["brName"]+" to an electric chair...")
input("50,000 Volts coursing through his body...")
input(data["name"]+": I'm here to make sure that doesn't happen.")
print()
print("==============")
print("─────████─────")
print("────█╬░░╬█────")
print("────█░░░░█────")
print("─────█░░█─────")
print("──────██──────")
print("────██░░██────")
print("───█░░░░░░█───")
print("───█░░░░░░█───")
print("───█░░░░░░█───")
print("==============")
print()
input("12 days ago, my brother preformed the greatest break-out in history and escaped the imfamous 'Cavacademy',")
input("the number one school for naughty, thieving little rascals.")
print()
print("=======================================")
print("░░░░░░░░░░░░░░░░░▄█░░░░░░░░░░░░░░░░░░░░")
print("▀▀▀█▄▄▄░░░░░░░▄█▀░░░░░░░░░░░░░░░░░░░░░░")
print("░░░░░░░▀▀█▄█▀▀░░░░░▄░░░░███████████████")
print("▀▀▀▀█▀▀▀▀░▐███▀▀▀▀░░░░░████────────────")
print("█░░░▌░░░░░░▌░▀█▄░░░░░░░███▌──┼┼┼┼┼┼┼┼──")
print("▌▀▀▀█░░░░░░▄▄░░░█░░░░░░███───┼┼┼┼┼┼┼┼──")
print("▀▀▀▀█░░░░░░░░▀▀█▀░░░░░░██▌─▄▄▄▄────────")
print("░░░░░▀▀█▀▀▀▀█▀▀░░░░░░░░██▌█░░░░▀█──────")
print("░░▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀░░░░░░██▌▌░███░▐▌─────")
print("░░░░░░░░░░░░░░░░░░░░░░░██─▌░▄█▄░▐──────")
print("░░░░░░░░░░░░░░░░░░░░░░▐██─▌▀░█░▀░▌─────")
print("░░░░░░░░░░░░░░░░░░░░░░░█▌─▌░▐░▌░░▌─────")
print("=======================================")
print()
input("Upon his escape, He was quickly abducted by a mysterious figure, known as L. Cole.")
input(data["brName"]+" was placed behind bars, trapped in the inescapable labyrinth known as the 'A.O.R.T.A Juvenile Detention Centre' for Misbehaved younglings.")
input('He was doomed for death. The place hosted some of the nastiest, most devious boys humanity can produce.')
input("They say it is impossible to escape...")
input('...')
input("..Not if you designed the place it isn't.")
print()
print("=======================================================================")
print("░█████╗░░█████╗░██████╗░████████╗░█████╗░░░░░░░░█████╗░██████╗░███████╗")
print("██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗░░░░░░██╔══██╗╚════██╗╚════██║")
print("███████║██║░░██║██████╔╝░░░██║░░░███████║█████╗██║░░██║░█████╔╝░░░░██╔╝")
print("██╔══██║██║░░██║██╔══██╗░░░██║░░░██╔══██║╚════╝██║░░██║░╚═══██╗░░░██╔╝░")
print("██║░░██║╚█████╔╝██║░░██║░░░██║░░░██║░░██║░░░░░░╚█████╔╝██████╔╝░░██╔╝░░")
print("╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░░░╚═╝░░░")
print("=======================================================================")
print()
time.sleep(5)

#game loop
while True:
    while data["cell"]:
        input("!! CELL !!")
        print("============================================================================================================")
        print("███▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████▒▒▒▒▒▒▒▒▒▒▒█")
        print("██▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▌█▒▒▒▒▒▒▒▒▒▒▒▒▒█")
        print("█▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄███▀▀██▀▀██▀▀█▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒█")
        print("█▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐░░░█▌░░▐█░░█▌░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████─────────███▒▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒█")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐░░░█▌░░▐█░░█▌░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██────────────────███▒▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌░░█░░░▐█░░█▌░░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██───────────────────███▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀▀▀█▄██▄▄█▄▄▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──────██████████────██▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████││││││││██████▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒██│││││││││││││││██▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▒▒▒▒▒▒▒▒▒█▄░▄█▒▒███│││││││││││││││██▒▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌──▄▄▐▒▒▒▒▒▒▒▒▒█░╬░█▒▒█░██│││││││││││││││██▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒█─╬───╬─█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────▐▒▒▒▒▒▒▒▒▒▒███▒▒▒█░░███││││││││││││││█▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▒▒▒▒▒█───═───█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▄▄▄▄▄█▒▒▒▒▒▒▒▄██│││█▄▄██░░░█████████████████▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██═══██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█─███─█▒▒▒▒▒▒▐═█│││││█═▌█░░░░░█░░░░░░░░░░█░░█▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒▒▒▒█║█▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒█─███─█▒▒▒▒▒▒█═█│││││█═▌████████████████░█░░█▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▐▒▒▒▒▒▒██║║║██▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒█──█──█▒▒▒▒▒▒█▄█│││││█▀▒██────█─────────██░░█▒▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▐█▒▒███║║║║║║║███▒▒▒▒▒▒██▒▒▒▒▒▒▐█───█▌▒▒▒▒▒▒▒░███████▒▒█─────█─────────██░██▒▐██▒▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▐███││█║║║║║║║█││██▀▀▀▀█▄▄▄▄▄▄▄▐─███─▌▄▄▄█▄▄▄░█──█──█▄█████──█─────────██▄█▄▄▐███▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▀▀░█││█║║║║║║║█││█░░░░░░░░░░▀░░▐─────▌░░░░░░░░█──█──█░░██████████████████░█░░▀███▒▒▒▒▒▒▒▒▒▒▒")
        print("▒▒▒▒▒▒▒▒▒▒▒▒▒▄▀░░░░█││█║║║║║║║█││█░░░░░░░░░░░░░░░░░░░░░░▒░░░░░█▄▄█▄▄█░░███│││█││││││││││█░█░░░░▀█▒▒▒▒▒▒▒▒▒▒█")
        print("▒██▒▒█▒▒▒▒▄▀▀░░░░░░████║║║║║║║████░░░░░▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒░░▒░██││││█││││││││││███░░░░░░▀██████▒▒▒█")
        print("▒█▒▒▒█▒▒▄█░░░░░░░░░═══█║║║║║║║█═══░░░░▒▒▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒░██││││█│││││││││││██░░░░▒░░░█████▒▒▒█")
        print("▒█▒▒█▒█▀░░░░░░░▒▒░░░░░█████████░░░░░░▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒░░░░░░░▒▒░░░██││█│││││││││││││█░░░░▒▒░░░░███▒▒▒█")
        print("▒█▒█▒█░░░░░░░░▒▒▒░░░░░█║║║█║║║█░░░░░▒░▒▒░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░░░░░░▒▒░░██││█│││││││││││││█░░░░░▒▒░░░░█▄▒▒▒█")
        print("▒██▒▄█░░░░░░░░▒▒▒░░░░░█║║║█║║║█░░░░░░▒▒▒░░░░░░░░░░░░░░░░░░▒▒▒░░░░░░░▒▒░░░█││█│││││││││││││█░░░░░▒▒▒░░░░░█▒▒▒")
        print("██▒█░░░░░░░░░░░▒▒░░░░░█║║║█║║║█░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░█│█│││││││││││││██░░░░▒▒▒▒░░░░░▀█▒")
        print("█▄█░░░░░░░░░░░░░░░░░░░█┼┼┼█┼┼┼█░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████████████████░░░░▒▒▒░░░░░░░░▌")
        print("============================================================================================================")
        print("Inventory:",*data["inventory"], sep=', ')
        if data["pillowInventory"]:
            print("Pillow Inventory: ",*data["pillowInventory"], sep=', ')
        print("============================================================================================================")
        print("A - Toilet")
        print("B - Cellmate")
        print("C - Bunk beds")
        print("D - Cracks")
        print("E - Bars")
        print("============================================================================================================")
        choice = str(input("> ")).lower()
        if choice == "a":
            print("It's a toilet!")
            time.sleep(2)
            print("===============================")
            print("A - Flush")
            print("B - Let her rip")
            print("===============================")
            choice = str(input("> ")).lower()
            if choice == "a":
                print("It flushed pretty well")
                time.sleep(1)
            if choice == "b":
                if jamesInteract:
                    print("J-Sack: Don't do that in front of me!")
                else:
                    print("???: Don't do that in front of me!")
                time.sleep(1)
        elif choice == "b":
            jamesInitiate = True
            while jamesInitiate:
                if not jamesInteract:
                    if not jamesName:
                        input("???: Who are YOU?")
                        print("=============================")
                        print("A - No, who are YOU?")
                        print("B - Your mum.")
                        print("C - Your cell mate?")
                        print("D - I don't care")
                        print("=============================")
                        choice = str(input("> ")).lower()
                        if choice == "a":
                            input("???: James Sackman, but around these parts, it's J-Sack... Got it fish?")
                            input(data["name"]+": Got it.")
                            jamesInteract = True
                            jamesInitiate = False
                        elif choice == "b":
                            input("???: No, my mum is at home eating Libby.")
                            print("===================================================")
                            print("A - What is a libby?")
                            print("B - I don't want to know what that is.")
                            print("===================================================")
                            choice = str(input("> ")).lower()
                            if choice == "a":
                                input("???: Sister.")
                        elif choice == "c":
                            input("???: And what is my cell mate's name??")
                            input(data["name"]+": Freddy McBumfuzzle")
                            jamesName = True
                        elif choice == "d":
                            jamesinitiate = False
                    else:
                        input("???: Ok, Freddy McBumfuzzle...")
                        print("=========================================")
                        print("A - Now, who are you?")
                        print("B - I do not care for you")
                        print("=========================================")
                        choice = str(input("> ")).lower()
                        if choice == "a":
                            input("???: James Sackman, but around these parts, it's J-Sack... Got it fish?")
                            input(data["name"]+": Got it.")
                            jamesInteract = True
                            jamesInitiate = False
                        elif choice == "b":
                            input('???: Ugh, fine... You do you buddy.')
                            jamesInitiate = False
                else:
                    if jamesName:
                        if not jamesKnife:
                            input("J-Sack: Hey, I like you kid. just incase you run into some nasty goons or violent COs, I've got a cool little knife i made back in the psych ward, ya want it?")
                            input("Aquired: Make-Shift Knife!")
                            data["inventory"].append("Make-Shift Knife")
                            input("J-Sack: Ya gotta keep yourself safe kid, they ain't playin' games.")
                            input("J-Sack: It's a rough place out there.")
                            input(data["name"]+": This'll come in handy...")
                            jamesKnife = True
                            jamesInitiate = False
                        else:
                            input("J-Sack: Take a walk kid. What you want, I don't have..")
                            jamesInitiate = False
                    else:
                        input("J-Sack: Who are YOU?")
                        print("=============================")
                        print("A - Your mum.")
                        print("B - Your cell mate?")
                        print("C - I don't care")
                        print("=============================")
                        choice = str(input("> ")).lower()
                        if choice == "a":
                            input("???: No, my mum is at home eating Libby.")
                            print("===================================================")
                            print("A - What is a libby?")
                            print("B - I don't want to know what that is.")
                            print("===================================================")
                            choice = str(input("> ")).lower()
                            if choice == "a":
                                input("???: Sister.")
                        elif choice == "b":
                            input("???: And what is my cell mate's name??")
                            input(data["name"]+": Freddy McBumfuzzle")
                            jamesName = True
                            jamesInitiate = False
                        elif choice == "c":
                            jamesInitiate = False
        elif choice == "c":
            input("I'm getting the bottom bunk, every new fish in AORTA gets put there...")
            print("==============================================================================")
            print("A - Look under bottom-bunk pillow")
            print("B - Look under top-bunk pillow")
            print("==============================================================================")
            choice = str(input("> ")).lower()
            if choice == "b":
                input(data["name"]+": A rusty wrench... Mysterious...")
                print("========================================")
                print("A - Inspect mystical wrench")
                print("B - Leave")
                print("========================================")
                choice = str(input("> ")).lower()
                if choice == "a":
                    input("You inspect the mysterious rusty wrench. Upon first glance, it appears that it is a normal tool in need of replacement.")
                    input("but on closer inspection, you notice that ther are glowing, cursed-looking engravings carved into the body of the wrench. you feel mesmerised...")
                    input("peculiar...")
            elif choice == "a":
                if not pillowUsed:
                    input(data["name"]+": It's my pillow, I can store contraband in here if I want to.")
                else:
                    input("Should I put something in here?")
                print("===========================================================================")
                print("A - Store Contraband")
                print("B - Leave")
                print("===========================================================================")
                choice = str(input("> ")).lower()
                if choice == "a":
                    pillowUsed = True
                    if data["inventory"]:
                        for item in data["inventory"]:
                            print("=============================")
                            print("A - Store "+item+"?")
                            print("B - Don't Store "+item+"?")
                            print("=============================")
                            choice = str(input("> ")).lower()
                            if choice == "a":
                                data["inventory"].remove(item)
                                data["pillowInventory"].append(item)
                                input("Stored "+item+"!")
                    else:
                        input(data["name"]+": I don't have anything to put in here")
        elif choice == "d":
            if not jamesInteract:
                input(data["name"]+": There are cracks on the wall, I wonder how long my weird cell-buddy has been in here...")
            else:
                input(data["name"]+": These walls aren't that durable if I remember correctly")
        elif choice == "e":
            input(data["name"]+": These bars lead to... Nowhere, there is literally no sign of the outside world when looking out these bars")
