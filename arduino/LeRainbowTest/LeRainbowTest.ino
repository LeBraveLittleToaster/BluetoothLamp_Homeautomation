#include <FastLED.h>

#define NUM_LEDS 112
#define DATA_PIN 4
#define SOUND_SENSOR_PIN 2

int mode = 0;
long modeTimer = 0;

uint8_t gHue = 0;

uint8_t gSat = 255;
uint8_t gVal = 255;

uint8_t gHueDelta = 1;

float gWaveRad = 0;

CRGB leds[NUM_LEDS];


void setup() {
  Serial.begin(9600);
  Serial.println("LED controller coming online...");
  
  digitalWrite(LED_BUILTIN, LOW);
  pinMode(SOUND_SENSOR_PIN, INPUT);
  
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  delay(500);
  setColor(0, NUM_LEDS, 75,0,255);
  FastLED.show();
  
  delay(500);
  
  setColor(0, NUM_LEDS, 255,255,255);
  FastLED.show();
  
  delay(500);
  
  setColor(0, NUM_LEDS, 0,0,0);
  FastLED.show();
  
  delay(500);
}

int incomingByte = 0;

//MODE and 6 x 0-255 values
int net_values[] = {0,0,0,0,0,0,0};

int read_counter = 0;
int MAX_AMOUNT_READ = 7;

boolean isReading = true;
boolean isLightUpdateNeeded = false; 

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read(); // read the incoming byte:
    delay(1);
    
    if(incomingByte != -1){
      if(isReading && incomingByte != '#'){
        net_values[read_counter] = incomingByte;
        read_counter++;
        if(read_counter >= MAX_AMOUNT_READ){
          isReading = false;
          isLightUpdateNeeded = true;
          
        }
      }else if(incomingByte == '#'){
        read_counter = 0;
        isReading = true;
        
      } 
    }
  }
  

  if(!isReading && isLightUpdateNeeded){
    isLightUpdateNeeded = false;
    setValues();
  }
  updateColors();
  
}


int readColor() {
  return Serial.read() * 2 % 255;
}

void updateColors() {
  switch (mode) {
    case 0:
      turnOff();
      break;
    case 1:
      setColor(0, NUM_LEDS, gHue, gSat, gVal);
      FastLED.show();
      break;
    case 2:
      modeColorWave(gHue);
      break;
    case 3:
      modeColorWaveFade();
      break;
    case 4:
      modeClicker(false, gHue);
      delay(25);
      break;
    case 5:
      modeClicker(true, 0);
      delay(7);
      break;
    case 6:
      modeColorFade();
      break;
    case 7:
      modeStarfallDown(0, 0);
      break;
    case 8:
      modeStarfallUp(0,0);
      break;
    case 9:
      modeAudioReactSquaresColor();
      break;
  }
}

void turnOff(){
  setColor(0, NUM_LEDS, 0,0,0);
  FastLED.show();
}

//Set gHueDelta to something greater or smaller to speed it
void modeColorFade(){
  delay(10);
  gHue += gHueDelta;
  setColor(0, NUM_LEDS, gHue, gSat, gVal);
  FastLED.show();
}

void modeColorWaveFade() {
  delay(10);
  gHue += gHueDelta;

  int x = 5;
  for(int i = 0; i < NUM_LEDS; i+=7){
    for(int ii = 0; ii < 7; ii++){
      uint8_t xHue = gHue + i * x;
       leds[i + ii] = CHSV(xHue, gSat, gVal);
    }
  }
  FastLED.show();
}

void modeClicker(bool isRainbow, int8_t hue) {

  if (isRainbow) {
    hue = random(0, 256);
  }
  if (random(0, 5) == 0) {
    leds[random(0, NUM_LEDS)] = CHSV( hue, gSat, gVal);
  }
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i].nscale8(230);
  }
  FastLED.show();
}

void modeColorWave(int hue) {
  int curWaveRad = gWaveRad;

  gWaveRad += 0.1;

  for(int i = 0; i < NUM_LEDS; i+= 7){
    int val = ((sin(curWaveRad) + 1) * 0.5) * 155 + 100;
    curWaveRad += 20;
    setColor(i, 7, hue, 255, val);
  }
  
  FastLED.show();
}

void modeStarfallDown(uint8_t hue, uint8_t sat){
  for(int i = NUM_LEDS - 7; i < NUM_LEDS; i++){
    leds[i].nscale8(230);
  }
  moveLineDown();
  for(int i = NUM_LEDS - 7; i < NUM_LEDS; i++){
    if(random(0,30) == 0){
      leds[i] = CHSV(hue,sat,255);
    }
  }
  FastLED.show();
  delay(40);
}

void modeStarfallUp(uint8_t hue, uint8_t sat){
  for(int i = 0; i < 7; i++){
    leds[i].nscale8(230);
  }
  moveLineUp();
  for(int i = 0; i < 7; i++){
    if(random(0,30) == 0){
      leds[i] = CHSV(hue,sat,255);
    }
  }
  FastLED.show();
  delay(40);
}


void modeAudioReactSquaresColor(){
  int sensorData = digitalRead(SOUND_SENSOR_PIN);

  if(sensorData == 1){
    Serial.println(sensorData);
    int randHue = random(0,255);
    setColor(0, NUM_LEDS, randHue, 255,255);
  }
  FastLED.show();
  delay(20);
}



void setColor(int offset, int count, int hue, int sat, int value) {
  for (int i = offset; i < offset + count; i++) {
    leds[i] = CHSV(hue, sat, value);
  }
}

void moveLineUp(){
  for(int i = (NUM_LEDS - 8); i >= 0; i--){
    leds[i + 7] = leds[i];
  }
  setColor(0, 7, 0,0,0);
}

void moveLineDown(){
  for(int i = 7; i < NUM_LEDS; i++){
    leds[i - 7] = leds[i];
  }
  setColor(NUM_LEDS - 7 , 7, 0,0,0);
}

void setValues(){
  mode = net_values[0];
  switch(mode){
    case 0:
      //turn off need no values
      break;
    case 1:
      gHue = net_values[1];
      gSat = net_values[2];
      gVal = net_values[3];
      break;
    case 2:
      gHue = net_values[1];
      gSat = net_values[2];
      gVal = net_values[3];
      break;
    case 3:
      gHue = net_values[1];
      gSat = net_values[2];
      gVal = net_values[3];
      break;
    case 4:
      gHue = net_values[1];
      gSat = net_values[2];
      gVal = net_values[3];
      break;
    case 5:
      gHue = net_values[1];
      gSat = net_values[2];
      gVal = net_values[3];
      break;
    case 6:
      gHue = net_values[1];
      gSat = net_values[2];
      gVal = net_values[3];
      break;
    case 7:
      //need no values
      break;
    case 8:
      //need no values
      break;
    case 9:
      //tbd
      break;
  }
}
