from machine import Pin, PWM

in3= Pin(15,Pin.OUT)
in4= Pin(2,Pin.OUT)
enb= PWM(Pin(0), freq=5000,duty_u16=2**16-1)


def Forward():
    in4.on()
    in3.off()
    #enb.on()
    enb.duty_u16(32768)
    return

def Backward():
    in4.off()
    in3.on()
    #enb.on()
    return
    