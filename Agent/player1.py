# from MessageController import MsgController
import sys
import time
# import numpy as np
import random

def Initialization(initMsg):
    msgElements = initMsg.split(' ')
    global mapHeight, mapWidth, playerX, playerY, playerHealth, playerBombRange, playerTrapCount, \
         vision, bombDelay, maxBombRange, deadzoneStartingStep, deadzoneExpansionDelay, maxStep

    # first initialization
    mapHeight = msgElements[1]
    mapWidth = msgElements[2]
    playerX = msgElements[3]
    playerY = msgElements[4]
    playerHealth = msgElements[5]
    playerBombRange = msgElements[6]
    playerTrapCount = msgElements[7]
    vision = msgElements[8]
    bombDelay = msgElements[9]
    maxBombRange = msgElements[10]
    deadzoneStartingStep = msgElements[11]
    deadzoneExpansionDelay = msgElements[12]
    maxStep = msgElements[13]

    return('init confirm')

def NoOpponentNoBox():
    # Random Walk
    return(int(random.random() * 5))

def BoxFinded(boxPositions):
    print(boxPositions)

def BothOpponentAndBox(opponentPosition, boxPositions):
    print(opponentPosition, boxPositions)

def JustOpponentVisited(opponentPosition):
    print(opponentPosition)

def FindBox(numVison, vision):
    # print("hello", numVison, vision)

    boxList = []
    for i in range(int(numVison)):
        x = vision[3 * i]
        y = vision[3 * i + 1]
        state = vision[3 * i + 2]
        
        if int(state) == 2:
            boxList.append((int(x), int(y)))

    return boxList 

def MsgController(msg):
    global gamePlaying

    msgElements = msg.split(' ')
    print(f'Message: {msg}', file=sys.stderr)

    # Game Initialization
    if msgElements[0] == "init":
        return Initialization(msg)
    
    # Game Termination
    elif msgElements[0] == "term":
        gamePlaying = False
        print(f'winner: {msgElements[2]}', file=sys.stderr)
    
    # Game Playing
    elif msgElements[-1] == "EOM":
        global stepCount
        stepCount = msgElements[0]
        # Opponent in Range
        if int(msgElements[8]) == 1:
            print(f'in Range', file=sys.stderr)
            global opponentX, opponentY, opponentHealth
            global opponentTrajectory 
            opponentTrajectory = []

            opponentX = msgElements[9]
            opponentY = msgElements[10]
            opponentHealth = msgElements[11]

            # save opponent trajectory
            opponentTrajectory.append((opponentX, opponentY, opponentHealth, stepCount))

            boxList = FindBox(msgElements[12], msgElements[13:-1])

            if boxList:
                # Both Visited
                BothOpponentAndBox((opponentX, opponentY, opponentHealth), boxList)
            else:
                # just Agent Visited
                JustOpponentVisited((opponentX, opponentY, opponentHealth))
    
        # Opponent out of Range
        elif int(msgElements[8]) == 0:
            print(f'out of Range', file=sys.stderr)
            boxList = FindBox(msgElements[9], msgElements[10:-1])
            if boxList:
                # Box Finded
                BoxFinded(boxList)
            else:
                # random walk
                return NoOpponentNoBox()
    
    # Error in Game
    else:
        return -1


gamePlaying = True

while(gamePlaying):
    msg = input()
    response = MsgController(msg)
    print(f'Response: {response}', file=sys.stderr)

    if response != -1:
        print(response)
    else:
        gamePlaying = False