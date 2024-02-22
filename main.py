from microdot import *
from machine import Pin
from utemplate import *

app = Microdot()
Response.default_content_type = 'text/html'

# Our LED Module
led_pin= Pin(2,Pin.OUT)


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

app.run()