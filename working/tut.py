from machine import Pin

bitZero= Pin(36,Pin.IN)
bitOne= Pin(39,Pin.IN)
bitTwo= Pin(34,Pin.IN)
bitThree= Pin(35,Pin.IN)

def update():
    # Read the state of each pin
    bit_zero_state = bitZero.value()
    bit_one_state = bitOne.value()
    bit_two_state = bitTwo.value()
    bit_three_state = bitThree.value()

    # Convert the bits to a decimal number
    res = bit_zero_state + bit_one_state * 2 + bit_two_state * 4 + bit_three_state * 8
    print (res)
    return res

