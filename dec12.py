import csv

with open('dec12.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\n')
    input = []
    for line in reader:
        input.extend(line)

print(input[0:10])

# start = [0, 0, 'E']    # x, y, face
# record = []
# record.append(start)
# ESWN = ['E', 'S', 'W', 'N']



def doActionB(action, currentCoorWaypoint, currentCoorShip):
    newCoorWaypoint = [0,0]
    newCoorShip = [0,0]
    direction = action[0]
    distance = action.strip(direction)
    differ = [currentCoorWaypoint[0]-currentCoorShip[0], currentCoorWaypoint[1]-currentCoorShip[1]]
    if direction == 'F':
        newCoorShip[0] = currentCoorShip[0] + differ[0] * int(distance)
        newCoorShip[1] = currentCoorShip[1] + differ[1] * int(distance)
        newCoorWaypoint[0] = newCoorShip[0] + differ[0]
        newCoorWaypoint[1] = newCoorShip[1] + differ[1]
    
    if direction == 'E' or direction == 'N':
        sign = 1
    if direction == 'W' or direction == 'S':
        sign = -1
    
    if direction == 'N' or  direction == 'S':
        newCoorWaypoint[0] = currentCoorWaypoint[0]
        newCoorWaypoint[1] = currentCoorWaypoint[1] + int(distance) * sign
        newCoorShip[0] = currentCoorShip[0] 
        newCoorShip[1] = currentCoorShip[1] 
    
    if direction == 'E' or direction == 'W':
        newCoorWaypoint[0] = currentCoorWaypoint[0] + int(distance) * sign
        newCoorWaypoint[1] = currentCoorWaypoint[1]
        newCoorShip[0] = currentCoorShip[0] 
        newCoorShip[1] = currentCoorShip[1] 
   
    if direction == 'R' or direction == 'L':
        newCoorShip[0] = currentCoorShip[0] 
        newCoorShip[1] = currentCoorShip[1] 
        turnR = [[differ[1], -1*differ[0]],[-1*differ[0], -1*differ[1]],[-1*differ[1], differ[0]]]
        turnL = [[-1*differ[1], differ[0]],[-1*differ[0], -1*differ[1]],[differ[1], -1*differ[0]]]
        times = int(int(distance)/90) - 1
        if direction == 'R':
            newCoorWaypoint[0] = currentCoorShip[0] + turnR[times][0]
            newCoorWaypoint[1] = currentCoorShip[1] + turnR[times][1]
        if direction == 'L':
            newCoorWaypoint[0] = currentCoorShip[0] + turnL[times][0]
            newCoorWaypoint[1] = currentCoorShip[1] + turnL[times][1]
    return  newCoorWaypoint, newCoorShip


waypointStart = [10, 1] # x, y
shipStart = [0, 0]    
# differ = [waypointStart[0]-shipStart[0], waypointStart[1]-shipStart[1]]
recordship = []
recordWp = []
recordship.append(shipStart)
recordWp.append(waypointStart)

# aa = doActionB(input[0], waypointStart, shipStart)
# print(aa)

# sample = ['F10','N3','F7','R90','F11']

for i, x in enumerate(input):
    # print(i, x)
    # print('ship: ', recordship[i], 'waypoint: ', recordWp[i])
    differ= [recordWp[i][0]-recordship[i][0], recordWp[i][1]-recordship[i][1]]
    # print('differ: ', differ)
    
    wpShip = doActionB(x, recordWp[i], recordship[i])
    recordWp.append(wpShip[0])
    recordship.append(wpShip[1])

    # print('new waypoint, new ship:',wpShip)
    # print('----------------------------')

# print(13464+33604) too high
# print(3194+13268) too low
# print(20290+2558)

# wx = 1
# wy = -10
# n=180
# for _ in range(int(n/90)):
#     print(wx, wy)
#     wx, wy = -wy, wx
#     print(wx, wy)






def doAction(action, currentCoor):
    newCoor = [0,0,0]
    direction = action[0]
    distance = action.strip(direction)
    if direction == 'R' or direction == 'L':
        da = int(int(distance)/90)
        for i, x in enumerate(ESWN):
            if currentCoor[2] == x:
                print(i,x )
                pos = (i+da)%4
                if direction == 'R':
                    # print(da, ESWN[i+(1+da)])
                    newCoor[2] = ESWN[pos]
                    break
                if direction == 'L':
                    newCoor[2] = ESWN[i-(da)]
                    break
        newCoor[1] = currentCoor[1]
        newCoor[0] = currentCoor[0]
    if direction == 'E' or direction == 'N':
        sign = 1
    if direction == 'W' or direction == 'S':
        sign = -1
    if direction == 'E' or direction == 'W':
        newCoor[0] = currentCoor[0] + int(distance) * sign
        newCoor[1] = currentCoor[1]
        newCoor[2] = currentCoor[2]
    if direction == 'N' or  direction == 'S':
        newCoor[0] = currentCoor[0] 
        newCoor[1] = currentCoor[1] + int(distance) * sign
        newCoor[2] = currentCoor[2]
    if direction == 'F':
        newCoor[2] = currentCoor[2]
        if currentCoor[2] == 'N':
            newCoor[0] = currentCoor[0] 
            newCoor[1] = currentCoor[1] + int(distance) 
        if currentCoor[2] == 'S':
            newCoor[0] = currentCoor[0] 
            newCoor[1] = currentCoor[1] - int(distance) 
        if currentCoor[2] == 'E' :
            newCoor[0] = currentCoor[0] + int(distance)
            newCoor[1] = currentCoor[1]
        if currentCoor[2] == 'W': 
            newCoor[0] = currentCoor[0] - int(distance)
            newCoor[1] = currentCoor[1]
    return newCoor

# firCoor = doAction(input[0], start)
# record.append(firCoor)
# print(record)

# for i, x in enumerate(input[1:]):
#     print(i, x)
#     print(record[i+1])
#     newCoor = doAction(x, record[i+1])
#     record.append(newCoor)
#     print(newCoor)
#     print('----------------------------')

# print(record)



