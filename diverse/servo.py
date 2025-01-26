from microbit import * 

# Fant disse verdiene på nett, men andre verdier fungerte bedre for oss
# Bruker write_analog med verdier 30 - 130 for å rotere mellom 0 og 180 grader
###########################################
# Servo control:                         #
# 50 = ~1 millisecond pulse all right    #   
# 75 = ~1.5 millisecond pulse center     # 
# 100 = ~2.0 millisecond pulse all left  #
##########################################

def servo(vinkel, pin=pin1):
    """ 
    Roter servo på pin (default er pin1) til vinkel mellom 0 og 180 grader
    """
    pin.set_analog_period(20)
    assert(vinkel >= 0 and vinkel <= 180)
    verdi = 30 + 100*vinkel/180
    pin.write_analog(verdi)

while True: 
    servo(0)
    sleep(800)
    servo(180)
    sleep(800)


