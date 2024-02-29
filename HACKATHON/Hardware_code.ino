#include <Adafruit_MLX90614.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <PulseSensorPlayground.h>

//Pin declaration

//Pulse pin
#define Pulse_pin 25

//water level pins
#define POWER_PIN 27
#define SIGNAL_PIN 35

//Pump Pins
#define motor1Pin1 14 
#define motor1Pin2 12 
#define enable1Pin 26

//Buzzer Pin
#define buzzer 19

//Setting Pulse Parameter
int pulse_threshold=500; 

//Class Initialisation
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
LiquidCrystal_I2C lcd(0x27,16,2);
PulseSensorPlayground pulseSensor;

//Setting motor parameter
const int freq = 30000;
const int pwmChannel = 0;
const int resolution = 8;
int dutyCycle = 150;

void setup() {
  //Serial Initialization
  Serial.begin(9600);
  while (!Serial);

  // Water level sensor pin initialization
  pinMode(POWER_PIN, OUTPUT);   // configure pin as an OUTPUT
  digitalWrite(POWER_PIN, LOW); // turn the sensor OFF

  //lcd initialization
  lcd.init();
  lcd.clear();         
  lcd.backlight();// Make sure backlight is on

  //Pulse sensor initialsation 
  pulseSensor.analogInput(Pulse_pin);   
  pulseSensor.setThreshold(pulse_threshold);
  // Double-check the "pulseSensor" object was created and "began" seeing a signal.
   if (pulseSensor.begin()) {
    lcd.print("We created a pulseSensor Object !");  //This prints one time at Arduino power-up,  or on Arduino reset.  
  }

  /*// Print a message on both lines of the LCD.
  lcd.setCursor(2,0);   //Set cursor to character 2 on line 0
  lcd.print("Hello World!");
  
  lcd.setCursor(2,1);   //Move cursor to character 2 on line 1
  lcd.print("ArogyaMitra");*/
   
 //Temperature sensor initialization
 lcd.print("Adafruit MLX90614 test");
  if (!mlx.begin()) {
    lcd.print("Error connecting to MLX sensor. Check wiring.");
    while(1);
  }

  //Driver Properties
  // sets the pins as outputs:
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(enable1Pin, OUTPUT);
  
  // configure LED PWM functionalitites
  ledcSetup(pwmChannel, freq, resolution);
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(enable1Pin, pwmChannel);

  //Buzzer initailization
}

void loop() {
  //Temperature sensor readings
  lcd.print("*F\tObject = "); Serial.print(mlx.readObjectTempF()); Serial.print("*F");
  Serial.println();

  //Buzzer
  if(mlx.readObjectTempF()>110){
    tone(buzzer,1500,200);
  }
  else{
    noTone(buzzer);
  }

  //Waterlevel Sensor
  digitalWrite(POWER_PIN, HIGH);  // turn the sensor ON
  delay(10);                      // wait 10 milliseconds
  int value = analogRead(SIGNAL_PIN); // read the analog value from sensor
  digitalWrite(POWER_PIN, LOW);   // turn the sensor OFF

  int level=map(value,0,1800,0,100);
  lcd.print("The water sensor value: ");
  lcd.println(value);

  lcd.print("The water level: ");
  lcd.println(level);

  //Buzzer
  if(level<25){
    tone(buzzer,1500,200);
  }
  else{
    noTone(buzzer);
  }

  //pulse sensnor 
  if (pulseSensor.sawStartOfBeat()) {
    int myBPM = pulseSensor.getBeatsPerMinute();
    lcd.print("BPM: ");                        
    lcd.print(myBPM);
  }

  //Peristaltic Pump
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);                            
  ledcWrite(pwmChannel, dutyCycle);
}
