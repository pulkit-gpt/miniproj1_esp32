from microdot import *	
from machine import Pin, PWM
from utemplate import *
import motor

app = Microdot()
Response.default_content_type = 'text/html'

# LED Module
# led_pin= Pin(2,Pin.OUT)
in3= Pin(15,Pin.OUT)
in4= Pin(2,Pin.OUT)
pwm_obj = PWM(Pin(0), freq=5000, duty_u16=2**16-1)

@app.route('/')
async def index(request):
    print("GREAT")
    return await Template('index.html').render(title='Hello')

@app.route('/on')
async def led_on(request):
    led_pin.on()
    return "Led turned on"

@app.route('/off')
async def led_off(request):
    print("LED OFF REQUEST")
    led_pin.off()
    return "Led turned off"

@app.route('/toggle')
async def toggle_led(request):
    print("Receive Toggle Request!")
    led_pin.value(not(led_pin.value()))
    return "OK"

@app.post('/forward')
async def pwm_forward(request):
    req = request.json
    duty = req["duty"]
    duty = int(duty)
    print("int dumblog: ", duty, "\n")
    in4.on()
    in3.off()
    pwm_obj.duty_u16(duty)

@app.post('/backward')
async def pwm_backward(request):
    req = request.json
    duty = req["duty"]
    duty = int(duty)
    print("int dumblog: ", duty, "\n")
    in4.off()
    in3.on()
    pwm_obj.duty_u16(duty)

@app.get('/whatpwm')
async def get_pwm(request):
    print("pwm is something like: ", int(pwm_obj.duty_u16()))

app.run()

