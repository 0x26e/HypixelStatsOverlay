#REALLY IMPORTANT PLEASE READ
#FIRST YOU MUST INSTALL THE LATEST VERSION OF PYTHON FROM python.org
#YOU NEED TO EITHER RUN THE modules.bat FILE OR DO THE FOLLOWING
#OPEN COMMAND PROMPT AND TYPE
#pip install requests
#pip install 



#PLACE YOUR UUID (WITH DASHES) INBETWEEN THE QUOTES IN THE NEXT LINE
uuid = "4aa19464-3860-42eb-8af9-63ff4114d377" 


#PLACE YOUR API KEY INBETWEEN THE QUOTES IN THE NEXT LINE
key = "60dc9492-3ebc-4657-8cc4-dfe171018353"

#HOW TO GET YOUR UUID AND API KEY
#STEP 1: GOTO NAMEMC.COM AND LOOK UP YOUR IGN (OR WHOEVER'S STATS YOUR PULLING)
#STEP 2: COPY YOUR UUID (WITH THE DASHES) AND PASTE IT IN THE 2ND LINE
#STEP 3: LOG ONTO HYPIXEL.NET AND TYPE /api new IN THE CHAT
#STEP 4: COPY THE KEY IT GIVES YOU AND PASTE IT IN THE 6TH LINE

#IF YOU WANT TO CHANGE THE SIZE OF THE TEXT MESS AROUND WITH THIS NUMBER
textSize = int(40.2)

#YOU CNA CHANGE THE COlOR OF THE TEXT BY EITHER PUTTING A HEX VALUE OR JUST TYPING "red"
textColor = "#09d2f6"

#DO NOT CHANGE ANYTHING UNDER THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING
#IF YOU HAVE ANY QUESTIONS/SUGGESTIONS COME JOIN AT discord.gg/Bu86veVgjT





from tkinter import *
import requests
import json
from pprint import pprint
import time



windowWidth = textSize * 12
windowHeight = textSize * 8



print("\n" * 27)


#while True:
#    try:
#        if "Win32Window" in str(gw.getWindowsWithTitle('Lunar')[0]):
#            print("Found Lunar!")
#            time.sleep(1)
#            break
#    except IndexError:
#        print("Cannot find Lunar!")
#        input("Press enter to exit")
#        exit()
#
#lunarWindow = gw.getWindowsWithTitle('Lunar')[0]
def warnUser():
    print("\n" * 27)
    print("                    **KEEP THIS WINDOW OPEN**                             **KEEP THIS WINDOW OPEN**")
    print("            **CLOSING THIS WINDOW CLOSES THE OVERLAY**            **CLOSING THIS WINDOW CLOSES THE OVERLAY**")
    print("\n" * 5)
    print("                  ******************************                      ******************************")
    print("                **YOU CAN MOVE THE WINDOW AROUND**                  **YOU CAN MOVE THE WINDOW AROUND**")
    print("             **BY CLICKING AND DRAGGING ON THE TEXT**             **BY CLICKING AND DRAGGING ON THE TEXT**")
    print("              **LOOK IN THE CODE TO CHANGE TEXT SIZE**            **LOOK IN THE CODE TO CHANGE TEXT SIZE**")
    print("                **********************************                  **********************************")
    print("\n" * 5)
    print("                    **KEEP THIS WINDOW OPEN**                             **KEEP THIS WINDOW OPEN**")
    print("           **CLOSING THIS WINDOW CLOSES THE OVERLAY**             **CLOSING THIS WINDOW CLOSES THE OVERLAY**")
    print("\n" * 5)

def statsCallMain():
    print("1: Duels")
    print("2: Bedwars")
    print("3: Skywars")
    userGame = input()

    if userGame == "duels" or userGame == "Duels" or userGame == "1":
        print("\n" * 27)
        statsCallDuels()
    elif userGame == "bedwars" or userGame == "Bedwars" or userGame == "2" or userGame == "bw" or userGame == "BW":
        warnUser()
        statsCallBedwars()
    elif userGame == "skywars" or userGame == "Skywars" or userGame == "3" or userGame == "sw" or userGame == "SW":
        warnUser()
        statsCallSkywars()    
    else:
        print("\n" * 27)
        print('Please try again')
        statsCallMain()

    #BEDWARS

def statsCallBedwars():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Bedwars"]["wins_bedwars"]) > 0:
            bedwarsWins = data["player"]["stats"]["Bedwars"]["wins_bedwars"]
    except KeyError:
        bedwarsWins = 0
    try:    
        if int(data["player"]["stats"]["Bedwars"]["losses_bedwars"]) > 0:
            bedwarsLosses = data["player"]["stats"]["Bedwars"]["losses_bedwars"]
    except KeyError:
        bedwarsLosses = 0
    try:    
        if int(data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]) > 0:
            bedwarsFinals = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
    except KeyError:
        bedwarsFinals = 0
    my_label.config(text="Bedwars Wins: " + str(bedwarsWins) + "\nBedwars Losses: " + str(bedwarsLosses) + "\n Bedwars Finals: " + str(bedwarsFinals))
    root.after(5000,statsCallBedwars)

    #SKYWARS

def statsCallSkywars():
    data = requests.get(url).json()
    print(data["player"]["stats"]["SkyWars"]["wins"])
    try:
        if int(data["player"]["stats"]["SkyWars"]["wins"]) > 0:
            skywarsWins = data["player"]["stats"]["SkyWars"]["wins"]
    except KeyError:
        skywarsWins = 0
    try:    
        if int(data["player"]["stats"]["SkyWars"]["losses"]) > 0:
            skywarsLosses = data["player"]["stats"]["SkyWars"]["losses"]
    except KeyError:
        skywarsLosses = 0
    try:    
        if int(data["player"]["stats"]["SkyWars"]["kills"]) > 0:
            skywarsKills = data["player"]["stats"]["SkyWars"]["kills"]
    except KeyError:
        skywarsKills = 0
    try:    
        if int(data["player"]["stats"]["SkyWars"]["deaths"]) > 0:
            skywarsDeaths = data["player"]["stats"]["SkyWars"]["deaths"]
    except KeyError:
        skywarsDeaths = 0
    my_label.config(text="Skywars Wins: " + str(skywarsWins) + "\nSkywars Losses: " + str(skywarsLosses) + "\n Skywars Kills: " + str(skywarsKills) + "\nSkywars Deaths: " + str(skywarsDeaths))
    root.after(5000,statsCallSkywars)



def statsCallDuels():
    print("1: Bridge")
    print("2: UHC")
    print("3: OP")
    print("4: Classic")
    print("5: Skywars")
    print("6: Sumo")
    print("7: Bow")
    print("8: BowSpleef")
    print("9: Nodebuff")
    print("10: Combo")
    print("11: Blitz")
    print("12: MegaWalls")

    userChoice = input()

    #BRIDGE DUELS
    if userChoice == "bridge" or userChoice == "Bridge" or userChoice == "1":
        statsCallBridge()

    #UHC DUELS
    elif userChoice == "uhc" or userChoice == "UHC" or userChoice == "2":
        statsCallUHC()

    #OP DUELS
    elif userChoice == "op" or userChoice == "OP" or userChoice == "3":
        statsCallOP()

    #CLASSIC DUELS
    elif userChoice == "classic" or userChoice == "Classic" or userChoice == "4":
        statsCallClassic()

    #SKYWARS DUELS
    elif userChoice == "skywars" or userChoice == "Skywars" or userChoice == "5" or userChoice == "sw" or userChoice == "SW":
        statsCallSkywars
    
    #SUMO DUELS
    elif userChoice == "sumo" or userChoice == "Sumo" or userChoice == "6":
        statsCallSumo()

    #BOW DUELS
    elif userChoice == "bow" or userChoice == "Bow" or userChoice == "7":
        statsCallBow()

    #BOWSPLEEF DUELS
    elif userChoice == "bowspleef" or userChoice == "BowSpleef" or userChoice == "8" or userChoice == "Bowspleef":
        statsCallBowSpleef()

    #NODEBUFF DUELS
    elif userChoice == "nodebuff" or userChoice == "Nodebuff" or userChoice == "9" or userChoice == "NoDebuff":
        statsCallNodebuff()

    #COMBO DUELS
    elif userChoice == "combo" or userChoice == "Combo" or userChoice == "10":
        statsCallCombo()  

    #BLITZ DUELS
    elif userChoice == "blitz" or userChoice == "Blitz" or userChoice == "11":
        statsCallBlitz()
    
    #MEGAWALLS DUELS
    elif userChoice == "megawalls" or userChoice == "Megawalls" or userChoice == "12" or userChoice == "MegaWalls":
        statsCallMegawalls()

    else:
        print("\n" * 27)
        print("Please make sure you spelt the game correctly!")
        statsCallMain()


def statsCallBridge():
    root.lift()
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["bridge_duel_wins"]) > 0:
            bridgeWins = data["player"]["stats"]["Duels"]["bridge_duel_wins"]
    except KeyError:
        bridgeWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["bridge_duel_losses"]) > 0:
            bridgeLosses = data["player"]["stats"]["Duels"]["bridge_duel_losses"]
    except KeyError:
        bridgeLosses = 0
    warnUser()
    root.wm_attributes("-topmost", 1)
    my_label.config(text="Bridge Wins: " + str(bridgeWins) + "\nBridge Losses: " + str(bridgeLosses))
    root.after(5000,statsCallBridge)

def statsCallUHC():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["uhc_duel_wins"]) > 0:
            uhcWins = data["player"]["stats"]["Duels"]["uhc_duel_wins"]
    except KeyError:
        uhcWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["uhc_duel_losses"]) > 0:
            uhcLosses = data["player"]["stats"]["Duels"]["uhc_duel_losses"]
    except KeyError:
        uhcLosses = 0
    warnUser()
    my_label.config(text="UHC Wins: " + str(uhcWins) + "\nUHC Losses: " + str(uhcLosses))
    root.after(5000,statsCallUHC)

def statsCallOP():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["op_duel_wins"]) > 0:
            opWins = data["player"]["stats"]["Duels"]["op_duel_wins"]
    except KeyError:
        opWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["op_duel_losses"]) > 0:
            opLosses = data["player"]["stats"]["Duels"]["op_duel_losses"]
    except KeyError:
        opLosses = 0
    warnUser()
    my_label.config(text="OP Wins: " + str(opWins) + "\nOP Losses: " + str(opLosses))
    root.after(5000,statsCallOP)

def statsCallClassic():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["classic_duel_wins"]) > 0:
            classicWins = data["player"]["stats"]["Duels"]["classic_duel_wins"]
    except KeyError:
        classicWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["classic_duel_losses"]) > 0:
            classicLosses = data["player"]["stats"]["Duels"]["classic_duel_losses"]
    except KeyError:
        classicLosses = 0
    warnUser()
    my_label.config(text="Classic Wins: " + str(classicWins) + "\nClassic Losses: " + str(classicLosses))
    root.after(5000,statsCallClassic)

def statsCallSW():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["sw_duel_wins"]) > 0:
            swWins = data["player"]["stats"]["Duels"]["sw_duel_wins"]
    except KeyError:
        swWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["sw_duel_losses"]) > 0:
            swLosses = data["player"]["stats"]["Duels"]["sw_duel_losses"]
    except KeyError:
        swLosses = 0
    warnUser()
    my_label.config(text="SW Wins: " + str(swWins) + "\nSW Losses: " + str(swLosses))
    root.after(5000,statsCallSW)

def statsCallSumo():
    data = requests.get(url).json()
    #Tries to get Sumo wins/losses if there aren't any set to 0
    try:
        if int(data["player"]["stats"]["Duels"]["sumo_duel_wins"]) > 0:
            sumoWins = data["player"]["stats"]["Duels"]["sumo_duel_wins"]
    except KeyError:
        sumoWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["sumo_duel_losses"]) > 0:
            sumoLosses = data["player"]["stats"]["Duels"]["sumo_duel_losses"]
    except KeyError:
        sumoLosses = 0
    warnUser()
    #Changes the text on the overlay
    my_label.config(text="Sumo Wins: " + str(sumoWins) + "\nSumo Losses: " + str(sumoLosses))
    #Updates the text every 5s
    root.after(5000,statsCallSumo)

def statsCallBow():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["bow_duel_wins"]) > 0:
            bowWins = data["player"]["stats"]["Duels"]["bow_duel_wins"]
    except KeyError:
        bowWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["bow_duel_losses"]) > 0:
            bowLosses = data["player"]["stats"]["Duels"]["bow_duel_losses"]
    except KeyError:
        bowLosses = 0
    warnUser()
    my_label.config(text="Bow Wins: " + str(bowWins) + "\nBow Losses: " + str(bowLosses))
    root.after(5000,statsCallBow) 

def statsCallBowSpleef():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["bowspleef_duel_wins"]) > 0:
            bowSpleefWins = data["player"]["stats"]["Duels"]["bowspleef_duel_wins"]
    except KeyError:
        bowSpleefWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["bowspleef_duel_losses"]) > 0:
            bowSpleefLosses = data["player"]["stats"]["Duels"]["bowspleef_duel_losses"]
    except KeyError:
        bowSpleefLosses = 0
    warnUser()
    my_label.config(text="BowSpleef Wins: " + str(bowSpleefWins) + "\nBowSpleef Losses: " + str(bowSpleefLosses))
    root.after(5000,statsCallBowSpleef) 

def statsCallNodebuff():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["no_debuff_duel_wins"]) > 0:
            nodebuffWins = data["player"]["stats"]["Duels"]["no_debuff_duel_wins"]
    except KeyError:
        nodebuffWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["no_debuff_duel_losses"]) > 0:
            nodebuffLosses = data["player"]["stats"]["Duels"]["no_debuff_duel_losses"]
    except KeyError:
        nodebuffLosses = 0
    warnUser()
    my_label.config(text="Nodebuff Wins: " + str(nodebuffWins) + "\nNodebuff Losses: " + str(nodebuffLosses))
    root.after(5000,statsCallNodebuff) 

def statsCallCombo():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["combo_duel_wins"]) > 0:
            comboWins = data["player"]["stats"]["Duels"]["combo_duel_wins"]
    except KeyError:
        comboWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["combo_duel_losses"]) > 0:
            comboLosses = data["player"]["stats"]["Duels"]["combo_duel_losses"]
    except KeyError:
        comboLosses = 0
    warnUser()
    my_label.config(text="Combo Wins: " + str(comboWins) + "\nCombo Losses: " + str(comboLosses))
    root.after(5000,statsCallCombo)   

def statsCallBlitz():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["blitz_duel_wins"]) > 0:
            blitzWins = data["player"]["stats"]["Duels"]["blitz_duel_wins"]
    except KeyError:
        blitzWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["blitz_duel_losses"]) > 0:
            blitzLosses = data["player"]["stats"]["Duels"]["blitz_duel_losses"]
    except KeyError:
        blitzLosses = 0
    warnUser()
    my_label.config(text="Blitz Wins: " + str(blitzWins) + "\nBlitz Losses: " + str(blitzLosses))
    root.after(5000,statsCallBlitz)

def statsCallMegawalls():
    data = requests.get(url).json()
    try:
        if int(data["player"]["stats"]["Duels"]["mega_walls_duel_wins"]) > 0:
            megawallsWins = data["player"]["stats"]["Duels"]["mega_walls_duel_wins"]
    except KeyError:
        megawallsWins = 0
    try:    
        if int(data["player"]["stats"]["Duels"]["mega_walls_duel_losses"]) > 0:
            megawallsLosses = data["player"]["stats"]["Duels"]["mega_walls_duel_losses"]
    except KeyError:
        megawallsLosses = 0
    warnUser()
    my_label.config(text="Megawalls Wins: " + str(megawallsWins) + "\nMegawalls Losses: " + str(megawallsLosses))
    root.after(5000,statsCallMegawalls)



#MAIN WINDOW
root = Tk()
root.title('Test Title')
root.geometry(str(windowWidth) + "x" + str(windowHeight))
#MAKE TRANSPARENT
root.wm_attributes('-transparentcolor', root['bg'])
root.wm_attributes("-topmost", 1)
#REMOVES TITLE BAR
root.overrideredirect(1)



#shitty click and drag function
def move(event):
    x, y = root.winfo_pointerxy()
    root.geometry(f"+{x}+{y}")

root.bind('<B1-Motion>',move)

#the window (i think?)
my_frame = Frame(root, width=windowWidth, height=windowHeight)
my_frame.pack(pady=20, ipady=20, ipadx=20)

#label that draws text
my_label = Label(my_frame, font=("Rockwell", textSize), fg=textColor)
my_label.pack(pady=20)

#hypixel api url
url = f"https://api.hypixel.net/player?key={key}&uuid={uuid}"
data = statsCallMain()

root.mainloop()
