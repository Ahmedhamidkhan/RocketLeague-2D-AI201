import Ball
import Players
import math

def isCollision(playerX,playerY,ballX,ballY):
    distance=math.sqrt((math.pow(playerX-ballX,2)) + (math.pow(playerY-ballY,2)))
