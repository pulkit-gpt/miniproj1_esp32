from microdot import *
from machine import Pin, PWM
from utemplate import *

app = Microdot()
Response.default_content_type = 'text/html'

# Our LED Module
led_pin= Pin(2,Pin.OUT)
pwm_obj = PWM(Pin(2), freq=5000, duty_u16=2**16-1)

@app.route('/')
async def index(request):
    return render_template('index.html', led_value=led_pin.value())

@app.route('/on')
async def led_on(request):
    led_pin.on()
    return "Led turned on"

@app.route('/off')
async def led_off(request):
    led_pin.off()
    return "Led turned off"


@app.route('/toggle')
async def toggle_led(request):
    print("Receive Toggle Request!")
    led_pin.value(not(led_pin.value()))
    return "OK"

@app.post('/pwm')
async def pwm_toggler(request):
    req = request.json	
    duty = req["duty"]
    print("dumblog: ", duty, "\n")
    duty = int(duty)
    print("int dumblog: ", duty, "\n") 
    pwm_obj.duty_u16(duty)

app.run()

