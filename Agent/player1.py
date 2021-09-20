# from MessageController import MsgController
import sys
import time.time

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
        # Opponent in Range
        if int(msgElements[8]) == 1:
            print(f'in Range', file=sys.stderr)
    
        # Opponent out of Range
        elif int(msgElements[8]) == 0:
            print(f'out of Range', file=sys.stderr)
    
    # Error in Game
    else:
        return 0


gamePlaying = True

while(gamePlaying):
    msg = input()
    respond = MsgController(msg)
    print(f'Respond: {respond}', file=sys.stderr)

    if respond != 0:
        print(respond)
    else:
        gamePlaying = False