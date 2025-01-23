# Your new file!
# Controlled robot for the 4tronix Bit:Bot and BBC Micro:Bit
# Author David Bradshaw 2018

from microbit import *
import radio

radio.on()
radio.config(channel=15)
radio.config(power=7)

robotType = ""
I2CADDR = 0x1c


def detectModel():  # Detects which model were using XL or classic
    global robotType
    try:
        value = i2c.read(28, 1, repeat=False)  # Read i2c bus
        robotType = "XL"  # If we can read it then it must be XL
        display.show("X")
    except:
        robotType = "classic"  # If we can't read it it must be classic
        display.show("C")      # or Micro:bit is unplugged
    sleep(1000)  # Do this so the user can see if the correct model is found

detectModel()


# Motor pins; these tell the motor to go
# forward, backwards or turn
if robotType == "classic":
    leftSpeed = pin0
    leftDirection = pin8
    rightSpeed = pin1
    rightDirection = pin12

else:  # Bit:Bot XL
    leftSpeed = pin16
    leftDirection = pin8
    rightSpeed = pin14
    rightDirection = pin12


# Motor control to tell the motor what direction and speed to move
def move(_leftSpeed, _rightSpeed, _leftDirection, _rightDirection):
    # speed values between 1 - 1023
    # smaller values == faster speed moving backwards
    # Smaller values == lower speeds when moving forwards
    # direction 0 == forwards, 1 == backwards
    leftSpeed.write_analog(_leftSpeed)    # Set the speed of left motor
    rightSpeed.write_analog(_rightSpeed)  # Set the speed of right motor
    if (_leftDirection != 2):
        leftDirection.write_digital(_leftDirection)  # left motor
        rightDirection.write_digital(_rightDirection)  # right motor


def drive(speed):
    if (speed > 0):
        move(speed, speed, 0, 0)  # move the motors forwards
    else:
        speed = 1023 + speed
        move(speed, speed, 1, 1)  # move the motors backwards


def sharpRight():
    move(100, 1023 + -200, 0, 1)


def sharpLeft():
    move(1023 + -200, 100, 1, 0)

def spin():
    move(1000, 23, 0, 1)

def gentleRight():
    move(350, 0, 0, 0)


def gentleLeft():
    move(0, 350, 0, 0)

def følgeLeft():
    move(0, 500, 0, 0)

def følgeRight():
    move(500, 0, 0, 0)

def coast():
    move(0, 0, 2, 2)


def stop():
    move(0, 0, 0, 0)
    
def getLine(bit):
    """
    Venstre = 0
    Høyre = 1
    """
    mask = 1 << bit
    value = 0
    try:
        value = i2c.read(I2CADDR, 1)[0]
    except OSError:
        pass
    if (value & mask) > 0:
        return 1
    else:
        return 0        

def linjefolger():
    if getLine(1) == 1:
        følgeRight()
    if getLine(0) == 1:
        følgeLeft()
    if getLine(0) == 0 and getLine(1) == 0:
        drive(200)
        


while True:
    
    incoming = radio.receive()
    if incoming is not None:
        if incoming == "F":
            drive(1023)
            display.show(Image.ARROW_N, loop=False, delay=10)
        elif incoming == "LJ":
            linjefolger()
            #spin()
        elif incoming == "L":
            gentleLeft()
            display.show(Image.ARROW_W, loop=False, delay=10)
        elif incoming == "R":
            gentleRight()
            display.show(Image.ARROW_E, loop=False, delay=10)
        elif incoming == "B":
            drive(-1023)
            display.show(Image.ARROW_S, loop=False, delay=10)
        elif incoming == "S":
            stop()
            display.show(Image.SKULL, loop=False, delay=10)
