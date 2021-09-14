from MessageController import MsgController

gamePlaying = True


while(gamePlaying):
    msg = input()
    respond = MsgController(msg)

    if respond != 0:
        print(respond)
    
    gamePlaying = False