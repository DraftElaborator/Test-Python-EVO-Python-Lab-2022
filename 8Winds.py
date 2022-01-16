def direction(facing, turn):
    # your smart code here
    L = ["N","NE","E","SE","S","WS","W","NW"]
    if (type(turn) == int and -1080 < turn < 1080 and turn % 45 == 0):
        if facing in L:
            currentPosition = L.index(facing)
            numTurn = turn // 45
            newPosition = (currentPosition + numTurn) % len(L)
        else:
            return "facing is not in list of wind directions"
    else:
        return "turn must be a number multiple of 45, between -1080 and 1080"
    return L[newPosition]

