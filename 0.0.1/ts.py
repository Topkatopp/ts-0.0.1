import keyboard
import time
import os

with open("textures\\player.txt", "r") as f:
    player = f.read()

with open("textures\\up.txt", "r") as f:
    uptext = f.read()

def cls():
    os.system("cls")

x = 0
y = 0

while True:
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    print(uptext)
    print("\n" * x + " " * y + player)
    if keyboard.is_pressed("UP") == True:
        x -= 1
    if keyboard.is_pressed("DOWN") == True:
        x += 1
    if keyboard.is_pressed("RIGHT") == True:
        y += 1
    if keyboard.is_pressed("LEFT") == True:
        y -= 1

    time.sleep(0.01)
    cls()
