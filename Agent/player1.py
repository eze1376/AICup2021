# from MessageController import MsgController
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

    print("init confirm")

def MsgController(msg):
    msgElements = msg.split(' ')
    # print(msgElements)
    if msgElements[0]=="init":
        return("init confirm")
    else:
        return 0



initMsg = input()
Initialization(initMsg)


gamePlaying = True


while(gamePlaying):
    msg = input()
    respond = MsgController(msg)

    if respond != 0:
        print(respond)
    
    gamePlaying = False