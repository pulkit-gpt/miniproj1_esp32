from machine import Pin

in3= Pin(15,Pin.OUT)
in4= Pin(2,Pin.OUT)
enb= Pin(0,Pin.OUT)


def Forward():
    in4.on()
    in3.off()
    enb.on()
    return

def Backward():
    in4.off()
    in3.on()
    enb.on()
    return
    