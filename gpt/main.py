from machine import Pin,ADC
import motor
from microdot import *

app = Microdot()
Response.default_content_type = 'text/html'

# Our LED Module
led_pin= Pin(2,Pin.OUT)

@app.route('/')
async def index(request):
    return "hello"
@app.post('/forward')
async def pwm_forward(request):
    req = request.json
    duty = req["duty"]
    duty = int(duty)
    print("int dumblog: ", duty, "\n")
    motor.Forward(duty)

@app.post('/backward')
async def pwm_backward(request):
    req = request.json
    duty = req["duty"]
    duty = int(duty)
    print("int dumblog: ", duty, "\n")
    motor.Backward(duty)

@app.get('/whatpwm')
async def get_pwm(request):
    print("pwm is something like: ", int(motor.enb.duty_u16()))
    return f"Pwm is this {motor.enb.duty_u16()}"

app.run()