import time
from pathlib import Path
import os
import ast

def load():
    #globals
    global FirstTime
    global inventory
    inventory = []
   
    #opens the savedata file
    f = open("savedata.txt", "r")

    #opens the gamedata file
    g = open("gamedata.txt", "r")

    #read variables from savedata file
    for line in f:
        if("firsttime: " in line):
            FirstTime = line.replace("firsttime: ", "")
            FirstTime = ast.literal_eval(FirstTime.replace("\n", ""))
        
        if("inventory: " in line):
            inventory = line.replace("inventory: ", "")
            inventory = ast.literal_eval(inventory.replace("\n", ""))
           
def save():
    #opens savedata file
    f = open("savedata.txt", 'w')
   
    #writes variables to savedata file
    f.write("firsttime: " + str(FirstTime) + "\n")
    
def saveData():
    #writes variables to gamedata file
    print("i save")
    g = open("gamedata.txt", 'w')

def resetSave():
    f = open("savedata.txt", "w")
    f.write("firsttime: True\n")
    f.close()

#start of game
savepath = Path("./savedata.txt")
datapath = Path("./gamedata.txt")

#checks if the savedata file exists and makes the file and adds default values
# if it does not exist
if(savepath.is_file() == False):    
    resetSave()
   
#checks if the gamedata file exists and makes it if it doesn't
if(datapath.is_file() == False):
    f = open("gamedata.txt", "w")
    f.close()

#loads saved data
load()
print("What is your name?")
brName = str(input("> ").capitalize())
time.sleep(2)
print("What is your brothers name?")
name = str(input("> ")).capitalize()
time.sleep(2)
print("Five days from now, They strap my brother "+brName+" to an electric chair...")
time.sleep(4)
print("50,000 Volts coursing through his body...")
time.sleep(3)
print(name+": I'm here to make sure that doesn't happen.")
time.sleep(6)
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
time.sleep(1)
print("12 days ago, my brother preformed the greatest break-out in history and escaped the imfamous 'Cavacademy',")
print("the number one school for naughty, thieving little rascals.")
time.sleep(8)
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
print("Upon his escape, He was quickly abducted by a mysterious figure, known as L. Cole.")
time.sleep(6)
print(brName+" was placed behind bars, trapped in the inescapable labyrinth known as the 'A.O.R.T.A Juvenile Detention Centre' for Misbehaved younglings.")
time.sleep(6)
print('He was doomed for death. The place hosted some of the nastiest, most devious boys humanity can produce.')
time.sleep(8)
print("They say it is impossible to escape...")
time.sleep(3)
print('...')
time.sleep(3)
print("..Not if you designed the place it isn't.")
time.sleep(3.5)
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