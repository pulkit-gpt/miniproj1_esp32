from machine import Pin,ADC
import motor
import microdot

app = Microdot()
Response.default_content_type = 'text/html'

# Our LED Module
led_pin= Pin(2,Pin.OUT)


@app.route('/')
async def index(request):
    return "hello"

@app.route('/on')
async def led_on(request):
    motor.Forward
    return "Motor Forward"

@app.route('/off')
async def led_off(request):
    motor.Backward
    return "Motor Backward"

app.run()
