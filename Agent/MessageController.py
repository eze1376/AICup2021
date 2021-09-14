def MsgController(msg):
    msgElements = msg.split(' ')
    # print(msgElements)
    if msgElements[0]=="init":
        return("init confirm")
    else:
        return 0