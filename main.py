import os
import platform
import keyboard
import time

room_width = 100
room_height = 40
room = []

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')

def fillRoom():
    room.clear()
    for _ in range(0, room_height):
        r = []
        for _ in range(0, room_width):
            r.append("-")
        room.append(r)

def printRoom():
    for i in room:
        toPrint = ""
        for j in i:
            toPrint += j
        print(toPrint)

def drawRectangle(x, y, width, height):
    for j in range(x, x + width):
        for i in range(y, y + height):
            if i < 0:
                continue
            if j < 0:
                continue
            if i >= room_height:
                continue
            if j >= room_width:
                continue

            room[i][j] = "X"

def checkCollision(x, y, width, height):
    for j in range(x, x + width):
        for i in range(y, y + height):
            if i < 0:
                continue
            if j < 0:
                continue
            if i >= room_height:
                continue
            if j >= room_width:
                continue

            if room[i][j] == "X":
                return True
    return False

fillRoom()

start = time.clock()

direction1 = 0
speed1 = 8
position1 = 2

direction2 = 0
speed2 = 8
position2 = 2

positionBallX = room_width / 2
positionBallY = room_height / 2
speedBallX = 5
speedBallY = 5

while True:
    end = time.clock()
    diff = end - start
    start = end

    #Fisica de controles
    if keyboard.is_pressed('w'):
        direction2 = -1
        direction1 = -1
    else:
        if keyboard.is_pressed('s'):
            direction2 = 1
            direction1 = 1
        else:
            direction2 = 0
            direction1 = 0

    #Borrado de la room
    fillRoom()

    #Fisicas
    position1 += speed1 * diff * direction1
    drawRectangle(3, int(position1), 2, 10)

    position2 += speed2 * diff * direction2
    drawRectangle(room_width - 6, int(position2), 2, 10)

    positionBallX += speedBallX * diff
    positionBallY += speedBallY * diff

    #Fisica de la pelota

    if positionBallX < 0 or positionBallX >= room_width:
        speedBallX *= -1

    if positionBallY < 0 or positionBallY >= room_height:
        speedBallY *= -1

    if checkCollision(int(positionBallX), int(positionBallY), 3, 3):
        speedBallX *= -1

    drawRectangle(int(positionBallX), int(positionBallY), 3, 3)

    #Render de la room
    clear()
    printRoom()

