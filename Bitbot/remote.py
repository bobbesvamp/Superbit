from microbit import *
import radio

radio.on()
radio.config(channel=15)
radio.config(power=7)

while True:
    y_strength = accelerometer.get_y()
    Xstyrke = accelerometer.get_x()
    txMsg = ""
    if y_strength < 0 and button_a.is_pressed() and button_b.is_pressed():
        txMsg = "B"
        display.show(Image.ARROW_S, loop=False, delay=10)
    elif Xstyrke > 0 and button_a.is_pressed() and button_b.is_pressed():
        txMsg = "LJ"
        display.show(Image.DUCK, loop=False, delay=10)
    elif button_a.is_pressed() and button_b.is_pressed():
        txMsg = "F"
        display.show(Image.ARROW_N, loop=False, delay=10)
    elif button_a.is_pressed():
        txMsg = "L"
        display.show(Image.ARROW_W, loop=False, delay=10)
    elif button_b.is_pressed():
        txMsg = "R"
        display.show(Image.ARROW_E, loop=False, delay=10)
    else:
        txMsg = "S"
        display.show(Image.STICKFIGURE, loop=False, delay=10)
    radio.send(txMsg)
    sleep(10)
