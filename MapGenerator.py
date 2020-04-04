import random
import math

# random.seed(42)

#list declaration (duh)
array = []

#array dimensions
width = 15
height = 42

for p in range(width*height):
    # print(p)
    array.append('O')

cursorX = 0
cursorY = 0

cursorX = int(math.ceil(random.uniform(2, width-3)))
cursorY = int(math.ceil(random.uniform(2, height-3)))

print(width)
print(height)
print(cursorX)
print(cursorY)

pathMaxLength = width

direction = int(random.uniform(0,4))
print('Direction: ',direction)

moves = int(random.uniform(pathMaxLength/4,pathMaxLength))

paths = 1+ int(random.uniform(height/2,height))+ int(random.uniform(1,width))
while(paths>0):
    moves -=1
    if(moves<1):
        moves = int(random.uniform(pathMaxLength/4,pathMaxLength))
        paths -= 1
        direction = int(random.uniform(0,4))

    oldX = cursorX
    oldY = cursorY

    if direction==0:
        cursorY-=1
    elif direction==1:
        cursorX+=1
    elif direction==2:
        cursorY+=1
    else :
        cursorX-=1

    if cursorX<2 or cursorX>width-2:
        cursorX = oldX
        moves = int(random.uniform(pathMaxLength/4,pathMaxLength))
        direction = int(random.uniform(0,4))
    if cursorY<2 or cursorY>height-2:
        cursorY = oldY
        moves = int(random.uniform(pathMaxLength/4,pathMaxLength))
        direction = int(random.uniform(0,4))

    #if cursorX*cursorY>-1 and cursorX*cursorY<100:
    array[cursorX + width*cursorY ] = '.'


for x in range(width):
    for y in range(height):
        print(array[x + width*y], end = '')
    print('')

rooms = int(random.uniform(width/2,width*2))

roomMaxWidth = width/2
roomMaxheight = height/2

roomMinWidth = 4
roomMinHeight = 4

while(rooms>0):
    rooms -= 1
    hallFound = False
    roomFound = False
    #get random position for room upper left corner
    roomPosX = int(random.uniform(1,width-2))
    roomPosY = int(random.uniform(1,width))

    roomWidth = int(random.uniform(roomMinWidth,roomMaxWidth))
    roomHeight = int(random.uniform(roomMinHeight,roomMaxheight))

    # see if the room connects to a hallway and doesn't overlap another room
    for x in range(roomPosX, roomPosX+roomWidth):
        for y in range(roomPosY, roomPosY+roomHeight):
            if(array[x + width*y ] == '.'):
                hallFound = True
            if(array[x + width*y ] == 'R'):
                roomFound = True

    #If we can place a room then place a room
    if roomFound == False and hallFound == True :
        for x in range(roomPosX, roomPosX+roomWidth):
            for y in range(roomPosY, roomPosY+roomHeight):
                #if x>0 and x<width-1 and y>0 and y<height-1:
                if x + y*cursorY <100:
                    array[x + y*cursorY ] = 'R'

for x in range(0,width):
    for y in range(0,height):
        print(array[x + width*y], end = '')
    print('')