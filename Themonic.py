import random
import math
import time
import os
import sys
import json
#REMEMBER TO ADD SOMETHING THAT CLEARS THE UI EVERYTIME A FUNCTION ENDS SO WE DONT GET 20 MILLION SHOPS WHEN WE BUY 4 POTIONS
# This function defines the enemies and their stats
class enemy:
    def __init__(self,name,level,attack,health):
        self.name = name
        self.level = level
        self.attack = attack
        self.health = health
#This function defines the player and their stats
class player:
    def __init__(self, name, attack, health, class_, level, experience, gold):
        self.name = name
        self.attack = attack
        self.health = health
        self.class_ = class_
        self.level = level
        self.experience = experience
        self.gold = gold
#This lists the price of the items
class items:
    def __init__(self, smallPotion, bigPotion, weaponUpgrade, armorUpgrade,):
        self.smallPotion = smallPotion
        self.bigPotion = bigPotion
        self.weaponUpgrade = weaponUpgrade
        self.armorUpgrade = armorUpgrade
#This function creats the starting stats for the player and asks for character name
def startStats():
    global p1
    global sellitem
    global experienceNeeded
    sellitem = items({"buy":5,"sell":1},{"buy":10,"sell":5},50,50,)
    createinventory()
    createWorldProgress()
    try:
        if classchoice == "warrior":
            p1 = player("temp",2,15,"warrior",0,0,2000)
        elif classchoice == "assassin":
            p1 = player("temp",4,7,"assassin",0,0,0)
        else:
            p1 = player("temp",0,0,"temp",0,0,0)
    except:
        print("FAIL")
    experienceNeeded = 95 + math.exp(p1.level/3)
    print("please choose a name for your character")
    p1.name = input()
    print("Hello" , p1.name , "and welcome to the world of Themonic")
    input("Press enter to continue")
    menu()
def createWorldProgress():
    global world1Progress
    global world2Progress
    global world3Progress
    global world4Progress
    global world5Progress
    global world6Progress
    global world7Progress
    global world8Progress
    global world9Progress
    global world10Progress
    world1Progress = 1
    world2Progress = 1
    world3Progress = 1
    world4Progress = 1
    world5Progress = 1
    world6Progress = 1
    world7Progress = 1
    world8Progress = 1
    world9Progress = 1
    world10Progress = 1
#This function checks if the player's exp is high enough to level up
#EXP formula is bad right now. needs to change
def expCheck():
    global experienceNeeded
    if p1.level <= 20:
        experienceNeeded = 95 + math.exp(p1.level/3)
    else:
        experienceNeeded = 100 + math.exp(p1.level/3.5)
    if p1.experience >= experienceNeeded:
        levelUp()
#This function levels up the player and boosts the stats
def levelUp():
        p1.level += 1
        p1.experience = p1.experience-experienceNeeded
        print("Level up!")
        p1.health += 5
        p1.attack += 2
#This function asks the player what class they want to play as
def classes():
    print("Please choose a class for info")
    print("(W)arrior or (A)ssassin")
    classInfo = input().lower()
    if classInfo == "w":
        warrior()
    elif classInfo == "a":
        assassin()
    else:
        classes()
#Describes the warrior class and gives the player the class warrior
def warrior():
    global classchoice
    print("A warrior uses brute force and strength to march down their enemies")
    print("Warriors have enhanced health, but lower attack")
    print("Favorite weapon is a sword")
    print("Would you like to play as the mighty warrior?")
    while True:
        print("[Y] or [N]")
        characterchoice = input().lower()
        if characterchoice == "y":
            print("You have chosen to become a warrior")
            classchoice = "warrior"
            break
        elif characterchoice == "n":
            classes()
            break
        else:
            continue
    startStats()
#Describes the assassin class and gives the player the class assassin
def assassin():
    global classchoice
    print("Assassins lurk in the dark and kill their prey with great speed and skill")
    print("Assassins have increased attack, but lower health")
    print("Favorite weapon is a dagger")
    print("Would you like to play as the cunning assassin?")
    while True:
        print("[Y] or [N]")
        characterchoice = input().lower()
        if characterchoice == "y":
            print("You have chosen to become an assassin")
            classchoice = "assassin"
            break
        elif characterchoice == "n":
            classes()
            break
        else:
            continue
    startStats()
#This function creates the inventory
#Needs to change to a dictionary where you see your item and a number besides it showing how many of that item you have
def createinventory():
    global inventory
    inventory =  {"small potion":0, "big potion":0}
#This function creates the shop so the player can buy and sell items
#This function also checks if inventory is full and whether the player can buy items
def shop():
    print("Hello there my friend!")
    print("(B)uy")
    print("(S)ell")
    print("(L)eave")
    buyOrSell = input().lower()
    t = True
    if buyOrSell == "l":
        t = False
        print("Alright")
        print("I hope to see you soon")
        menu()
    while t:
        print("You have", p1.gold , "coins")
        if buyOrSell == "b":
            print("What can i get ya?")
            print("[1] Weapon upgrade -" , sellitem.weaponUpgrade , "coins")
            print("[2] Armor upgrade -" , sellitem.armorUpgrade , "coins")
            print("[3] Small potion -" , sellitem.smallPotion["buy"] , "coins")
            print("[4] Big potion -" , sellitem.bigPotion["buy"] , "coins")
            print("[5] Exit")
            buyItem = input()
            if buyItem.isdecimal() == True:
                buyItem = int(buyItem)
                if buyItem == 1:
                    if p1.gold >= sellitem.weaponUpgrade:
                        print("You have purchased an upgrade for your weapon")
                        print("You now deal more damage in battle")
                        if p1.class_ == "assassin":
                            p1.attack += 3
                        elif p1.class_ == "warrior":
                            p1.attack += 1 
                        p1.gold -= sellitem.weaponUpgrade
                        sellitem.weaponUpgrade += 50
                    elif p1.gold < sellitem.weaponUpgrade:
                        print("You do not have enough coins to purchase this")
                elif buyItem == 2:
                    if p1.gold >= sellitem.armorUpgrade:
                        print("You have purchased an upgrade for you armor")
                        print("You now have more health in battle")  
                        if p1.class_ == "warrior":
                            p1.health += 3
                        else:
                            p1.health += 1
                        p1.gold -= sellitem.armorUpgrade
                        sellitem.armorUpgrade += 50
                    elif p1.gold < sellitem.armorUpgrade:
                        print("You do not have enough coins to purchase this")
                elif buyItem == 3:
                    if p1.gold >= sellitem.smallPotion["buy"]:
                        print("You have bought a small potion!")
                        p1.gold -= sellitem.smallPotion["buy"]
                        inventory["small potion"] = inventory["small potion"] + 1
                    elif p1.gold < sellitem.smallPotion["buy"]:
                        print("You do not have enough coins to purchase this")
                elif buyItem == 4:
                    if p1.gold >= sellitem.bigPotion["buy"]:
                        print("You have bought a big potion")
                        p1.gold -= sellitem.bigPotion["buy"]
                        inventory["big potion"] = inventory["big potion"] + 1
                    elif p1.gold < sellitem.bigPotion["buy"]:
                        print("You do not have enough coins to purchase this")
                elif buyItem == 5:
                    print("Alright")
                    shop()
                    break
                else:
                    print("please enter a valid answer")
                    continue
            else:
                print("Please enter a valid answer")     
        elif buyOrSell == "s":
            print("What do ya have for me?")
            j = 1
            for k in inventory:
                print("[" ,j, "]" , k, "- in inventory" , inventory[k], end ="")
                if k == "small potion":
                    print(" -" , sellitem.smallPotion["sell"], "coin")
                elif k == "big potion":
                    print(" -" , sellitem.bigPotion["sell"], "coins")
                j += 1
            print("[",j,"]", "Exit")
            sellAnswer = input()
            if sellAnswer.isdecimal() == True:
                l = 1
                for k in inventory:
                    if int(sellAnswer) == l:
                        if inventory[k] < 1:
                            print("You do not own this item")
                        else:
                            print("You sold 1", k)
                            if k == "small potion":
                                p1.gold += 1
                            elif k == "big potion":
                                p1.gold += 5
                            inventory[k] = inventory[k] -1
                    elif int(sellAnswer) == j:
                        print("Alright")
                        shop()
                        break
                    elif int(sellAnswer) < 1 or int(sellAnswer) > len(inventory):
                        print("Please enter a valid answer")
                    l += 1
                if sellAnswer == j:
                    break
            else:
                print("Please enter a valid answer")
        else:
            print("Please enter a valid answer")
            shop()
            break
#Introduces the player to the game if they choose new game in gamestart funcion
def introduction():
    print("Hello there my friend!")
    print("Before you start your journey I would like to get to know you a little better")
    input("Press enter to continue")
    classes()
#lets the player choose a world to play in
def worldSelector():
    while True:
        print("[1] World 1 | [2] World 2 |")
        print("------------|-------------|")
        print("[3] World 3 | [4] World 4 |")
        print("------------|----------   |")
        print("[5] World 5 | [6] World 6 |")
        print("------------|-------------|")
        print("[7] World 7 | [6] World 8 |")
        print("------------|-------------|")
        print("[9] World 9 |[10] World 10|")
        print("------------|-------------|")
        worldSelectorChoice = input()
        if worldSelectorChoice.isdecimal() == True:
            worldSelectorChoice = int(worldSelectorChoice)
            if worldSelectorChoice == 1:
                world1()
                break
            elif worldSelectorChoice == 2:
                world2()
                break
            elif worldSelectorChoice == 3:
                world3()
                break
            elif worldSelectorChoice == 4:
                world4()
                break
            elif worldSelectorChoice == 5:
                world5()
                break
            elif worldSelectorChoice == 6:
                world6()
                break
            elif worldSelectorChoice == 7:
                world7()
                break
            elif worldSelectorChoice == 8:
                world8()
                break
            elif worldSelectorChoice == 9:
                world9()
                break
            elif worldSelectorChoice == 10:
                world10()
                break
            else:
                print("Please choose a valid answer")
        else:
            print("Please choose a valid answer")
#UI of this needs to be cleaned up. is very ugly atm
#EXP formula and mob damage formula is quite bad
def battle():
    global world
    global world1Progress
    global world2Progress
    global world3Progress
    global world4Progress
    global world5Progress
    global world6Progress
    global world7Progress
    global world8Progress
    global world9Progress
    global world10Progress
    e1 = enemy("Mob",random.randint(BattleLevelDefiner - 1,p1.level + 2),0,0)
    e1.attack = random.randint(int(1 + e1.level*1.5),int(2 + e1.level * 2))
    e1.health = random.randint(10 + e1.level *2,15 + e1.level * 3)
    playerHealth = p1.health
    enemyHealth = e1.health
    print("An enemy has approached")
    while True:
        print("| World" , BattleLevelDefiner, "|")
        print("|",e1.name, "Health:", enemyHealth, "/", e1.health, "|")
        print("|",p1.name, "Health:", playerHealth, "/", p1.health, "|")
        print("|-------------------------------|")
        print("| [A]ttack | [I]ventory | [R]un |")
        print("|-------------------------------|")
        battleinput = input().lower()
        if battleinput == "a":
            playerattack = random.randint(int(0.8*p1.attack),p1.attack)
            enemyattack = random.randint(int(0.8*e1.attack),e1.attack)
            if enemyattack == 0:
                enemyattack += 1
            print("You dealt", playerattack, "damage")
            enemyHealth -= playerattack
            if enemyHealth <= 0:
                print("You won")
                goldGainedFromBattle = e1.level * random.randint(5,8)
                if e1.level <= 20:
                    expFromBattle = 2 * e1.level + 10
                else:
                    expFromBattle = 4 * e1.level + 10
                print("You gained", expFromBattle, "experience and", goldGainedFromBattle , "gold")
                p1.experience += expFromBattle
                expCheck()
                if world == 1:
                    world1Progress += 1
                    if world1Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world1Progress == 10:
                        print("You have completed world", world)
                        print("this is world 1")
                        menu()
                        break
                elif world == 2:
                    world2Progress += 1
                    if world2Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world2Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                elif world == 3:
                    world3Progress += 1
                    if world3Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world3Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                elif world == 4:
                    world4Progress += 1
                    if world4Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world4Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                elif world == 5:
                    world5Progress += 1
                    if world5Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world5Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                elif world == 6:
                    world6Progress += 1
                    if world6Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world6Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                elif world == 7:
                    world7Progress += 1
                    if world7Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world7Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                elif world == 8:
                    world8Progress += 1
                    if world8Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()  
                    elif world8Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                    break
                elif world == 9:
                    world9Progress += 1
                    if world9Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world9Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                elif world == 10:
                    world10Progress += 1
                    if world10Progress == 9:
                        print("A boss is coming: You should prepare yourself")
                        menu()
                        break
                    elif world10Progress == 10:
                        print("You have completed world", world)
                        menu()
                        break
                print("Would you like to continue on your adventure in world" , world,"?")
                print("[Y] or [N]")
                BattleEndChoice = input().lower()
                if BattleEndChoice == "y":
                    battle()
                elif BattleEndChoice == "n":
                    break
                else:
                    break
            print("You took", enemyattack, "damage")
            playerHealth -= enemyattack
            if playerHealth <= 0:
                print("You died")
                GoldLostWhenDead = int(p1.gold/5)
                print("You lost", GoldLostWhenDead, "gold")
                break   
        elif battleinput == "i":
            while True:
                var2 = 1
                for k in inventory:
                    print("[",var2,"]", k, "x" , inventory[k])
                    var2 += 1
                print("[",var2,"]", "Exit")
                inventoryBattleChoice = input()
                if inventoryBattleChoice.isdecimal() == True:
                    inventoryBattleChoice = int(inventoryBattleChoice)
                    if inventoryBattleChoice == var2:
                        break
                    elif inventoryBattleChoice == 1:
                        if inventory["small potion"] > 0:
                            print("Will you use the small potion?")
                            print("[Y] or [N]")
                            smallPotionUse = input().lower()
                            if smallPotionUse == "y":
                                print("You healed for", 10, "health")
                                playerHealth += 10
                                if playerHealth >= p1.health:
                                    playerHealth = p1.health
                                inventory["small potion"] = inventory["small potion"] - 1
                        else:
                            print("You do not own this item")
                    elif inventoryBattleChoice == 2:
                        if inventory["big potion"] > 0:
                            print("Will you use the big potion?")
                            print("[Y] or [N]")
                            bigPotionUse = input().lower()
                            if bigPotionUse == "y":
                                print("You healed for", 20, "health")
                                playerHealth += 10
                                if playerHealth >= p1.health:
                                    playerHealth = p1.health
                                inventory["big potion"] = inventory["big potion"] - 1
                        else:
                            print("You do not own this item")
                    else:
                        print("Please enter a valid answer")
                else:
                    print("Please enter a valid answer")
        elif battleinput == "r":
            RunAway = random.randint(1,3)
            if RunAway <= 2:
                print("You have ran away")
                menu()
                break
            elif RunAway == 3:
                print("You could not escape")
                enemyattack = random.randint(int(0.8*e1.attack),e1.attack)
                print("You took", enemyattack, "damage")
                playerHealth -= enemyattack
                if playerHealth <= 0:
                    print("You died") 
#Is the firs world of the game
#Introduces player to the world
#Goes to the except no matter what
#Perhaps make the worldprogress get defined in the charachter creation function
def world1():
    global BattleLevelDefiner
    global world1Progress
    global world
    BattleLevelDefiner = 1
    while True:
        world = 1
        print(world1Progress)
        if world1Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world1Progress ,"/10")
            print(world1Progress)
            if world1Progress == 9:
                BattleLevelDefiner = 3
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 1")
            print("Hit enter to continue")
            BattleLevelDefiner = 2
            input()
            battle()
            break
def world2():
    global BattleLevelDefiner
    global world2Progress
    global world
    BattleLevelDefiner = 3
    while True:
        if world1Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        world = 2
        if world2Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world2Progress ,"/10")
            if world2Progress == 9:
                BattleLevelDefiner = 5
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 2")
            print("Hit enter to continue")
            BattleLevelDefiner = 4
            input()
            battle()
            break
def world3():
    global BattleLevelDefiner
    global world3Progress
    global world
    BattleLevelDefiner = 5
    while True:
        if world2Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        world = 3
        if world3Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world3Progress ,"/10")
            if world3Progress == 9:
                BattleLevelDefiner = 7
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 3")
            print("Hit enter to continue")
            BattleLevelDefiner = 6
            input()
            battle()
            break
def world4():
    global BattleLevelDefiner
    global world4Progress
    global world
    BattleLevelDefiner = 7
    while True:
        if world3Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        world = 4
        if world4Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world4Progress ,"/10")
            if world4Progress == 9:
                BattleLevelDefiner = 9
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 4")
            print("Hit enter to continue")
            BattleLevelDefiner = 8
            input()
            battle()
            break
def world5():
    global BattleLevelDefiner
    global world5Progress
    global world
    BattleLevelDefiner = 9
    while True:
        if world4Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        world = 5
        if world5Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world5Progress ,"/10")
            if world5Progress == 9:
                BattleLevelDefiner = 11
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 5")
            print("Hit enter to continue")
            BattleLevelDefiner = 10
            input()
            battle()
            break
def world6():
    global BattleLevelDefiner
    global world6Progress
    global world
    BattleLevelDefiner = 11
    while True:
        if world5Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        world = 6
        if world6Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world6Progress ,"/10")
            if world6Progress == 9:
                BattleLevelDefiner = 13
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 6")
            print("Hit enter to continue")
            BattleLevelDefiner = 12
            input()
            battle()
            break
def world7():
    global BattleLevelDefiner
    global world7Progress
    global world
    BattleLevelDefiner = 13
    while True:
        if world6Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        world = 7
        if world7Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world7Progress ,"/10")
            if world7Progress == 9:
                BattleLevelDefiner = 15
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 7")
            print("Hit enter to continue")
            BattleLevelDefiner = 14
            input()
            battle()
            break
def world8():
    global BattleLevelDefiner
    global world8Progress
    global world
    BattleLevelDefiner = 15
    while True:
        if world7Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        world = 8
        if world8Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world8Progress ,"/10")
            if world8Progress == 9:
                BattleLevelDefiner = 17
                print("Boss battle is imminent")
            print("Hit enter to continue")
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 8")
            print("Hit enter to continue")
            BattleLevelDefiner = 16
            input()
            battle()
            break
def world9():
    global BattleLevelDefiner
    global world9Progress
    global world
    BattleLevelDefiner = 17
    while True:
        if world8Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        if world9Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world9Progress ,"/10")
            if world9Progress == 9:
                BattleLevelDefiner = 19
                print("Boss battle is imminent")
            print("Hit enter to continue")
            world = 9
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 9")
            print("Hit enter to continue")
            BattleLevelDefiner = 18
            world = 9
            input()
            battle()
            break
def world10():
    global BattleLevelDefiner
    global world10Progress
    global world
    BattleLevelDefiner = 19
    while True:
        if world9Progress < 10:
            print("You are not strong enough to enter this world")
            worldSelector()
            break
        if world10Progress < 10:
            print("Welcome to world 1")
            print("Progress:" , world10Progress ,"/10")
            if world10Progress == 9:
                BattleLevelDefiner = 21
                print("Boss battle is imminent")
            print("Hit enter to continue")
            world = 10
            input()
            battle()
            break
        else:
            print("Welcome to world 1")
            print("Progress: You have completed world 10")
            print("Hit enter to continue")
            BattleLevelDefiner = 20
            world = 10
            input()
            battle()
            break
def savegame():
    saveData = {
        "name" : p1.name,
        "attack" : p1.attack,
        "health" : p1.health,
        "_class" : p1.class_,
        "level" : p1.level,
        "experience" : p1.experience,
        "gold" : p1.gold,
        "smallPotion" : inventory["small potion"],
        "bigPotion" : inventory["big potion"],
        "weaponUpgradeCost" : sellitem.weaponUpgrade,
        "armorUpgradeCost" : sellitem.armorUpgrade,
        "world1Progress" : world1Progress,
        "world2Progress" : world2Progress,
        "world3Progress" : world3Progress,
        "world4Progress" : world4Progress,
        "world5Progress" : world5Progress,
        "world6Progress" : world6Progress,
        "world7Progress" : world7Progress,
        "world8Progress" : world8Progress,
        "world9Progress" : world9Progress,
        "world10Progress" : world10Progress
    }
    with open("ThemonicSaveFile.txt","w") as saveFile:
        json.dump(saveData,saveFile)
    saveFile.close()
    print("Game saved successfully!")
def loadgame():
    global classchoice
    global p1
    global sellitem
    global experienceNeeded
    createinventory()
    createWorldProgress()
    try:
        with open("ThemonicSaveFile.txt") as loadFile:
            loadedFile = json.load(loadFile)
            p1 = player(loadedFile["name"],loadedFile["attack"],loadedFile["health"],loadedFile["_class"],loadedFile["level"],loadedFile["experience"],loadedFile["gold"])
            sellitem = items({"buy":5,"sell":1},{"buy":10,"sell":5},loadedFile["weaponUpgradeCost"],loadedFile["weaponUpgradeCost"])
            inventory["small potion"] = loadedFile["smallPotion"]
            inventory["big potion"] = loadedFile["bigPotion"]
            world1Progress = loadedFile["world1Progress"]
            world2Progress = loadedFile["world2Progress"]
            world3Progress = loadedFile["world3Progress"]
            world4Progress = loadedFile["world4Progress"]
            world5Progress = loadedFile["world5Progress"]
            world6Progress = loadedFile["world6Progress"]
            world7Progress = loadedFile["world7Progress"]
            world8Progress = loadedFile["world8Progress"]
            world9Progress = loadedFile["world9Progress"]
            world10Progress = loadedFile["world10Progress"]
        if p1.level <= 20:
            experienceNeeded = 95 + math.exp(p1.level/3)
        else:
            experienceNeeded = 100 + math.exp(p1.level/3.5)
        print("Save file has been loaded")
        print("Press enter to continue")
        input()
        menu()
    except:
        print("You do not have a saved file on this computer")
        gameStart()
#This is very first function to use and is where players choose if they want to start a new game or play a saved file
def gameStart():
    print("[1] New game")
    print("[2] Continue")
    print("[3] Exit game")
    while True:
        gameStartChoice = input()
        if gameStartChoice.isdecimal() == True:
            if int(gameStartChoice) == 1:
                introduction()
                break
            elif int(gameStartChoice) == 2:
                loadgame()
            elif int(gameStartChoice) == 3:
                sys.exit()
            else:
                print("Please enter a valid answer")
        else:
            print("Please enter a valid answer")
#This function is the menu that will let the player go to every other place in the game
#The end of all other functions needs to redirect back to this function
def menu():
    while True:
        print("[1] Adventure | [2] Shop |")
        print("--------------|----------|")
        print("[3] Inventory | [4] Save |")
        print("--------------|----------|")
        print("[5] Stats     | [6] Exit |")
        print("--------------|----------|")
        menuchoice = input()
        if menuchoice.isdecimal() == True:
            menuchoice = int(menuchoice)
            #needs to either just start or continue adventure or let player choose the world to play
            #Needs work
            if menuchoice == 1:
                worldSelector()
            #Goes to shop
            elif menuchoice == 2:
                shop()
            #Goes to inventory
            #Needs to create a function that shows the invetory
            elif menuchoice == 3:
                showinventory()
            #Saves the game
            #needs work
            elif menuchoice == 4:
                savegame()
            #Goes to menu where player can see their stats
            #Needs work
            elif menuchoice == 5:
                showStats()
            #Exits the game
            #Needs to perhaps check if game has been saved and ask if they would like to save first
            #Needs work
            elif menuchoice == 6:
                sys.exit()
            else:
                print("Please enter a valid answer")
        else:
            print("Please enter a valid answer")
#Shows the inventory for the player
#Needs to also be where player can use items
def showStats():
    global experienceNeeded
    print(p1.name, "Stats:")
    print("Experience:" , p1.experience , "/" , experienceNeeded)
    print("Health:", p1.health)
    print("Attack:", p1.attack)
    print("Press enter to exit to menu")
    input()
def showinventory():
    var1 = 1
    print("Inventory:")
    for k in inventory:
        print("[",var1,"]", k, "x" , inventory[k])
        var1 += 1
    print("[",var1,"]", "Exit to menu")
    print(var1)
    while True:
        inventorychoice = input()
        if inventorychoice.isdecimal() == True:
            inventorychoice = int(inventorychoice)
            if inventorychoice == var1:
                menu()
                break
            else:
                print("Please enter a valid answer")
        else:
            print("Please enter a valid answer")
gameStart()