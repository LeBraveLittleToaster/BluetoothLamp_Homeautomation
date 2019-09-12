#include <FastLED.h>

#define NUM_LEDS 112
#define DATA_PIN 4

int mode = 0;

uint8_t gHue = 0;
uint8_t gVal = 0;
uint8_t gSat = 0;
uint8_t gFourthVal = 0;
uint8_t gFiftVal = 0;
uint8_t gSixtVal = 0;

uint8_t gHueDelta = 0;

float gWaveRad = 0;

int incomingByte = 0;
//MODE and 6 x 0-255 values
int net_values[] = {0,0,0,0,0,0,0};

int read_counter = 0;
int MAX_AMOUNT_READ = 7;

boolean isReading = true;
boolean isLightUpdateNeeded = false; 

CRGB leds[NUM_LEDS];


void setup() {
  Serial.begin(9600);
  Serial.println("LED controller coming online...");
  
  digitalWrite(LED_BUILTIN, LOW);
  pinMode(SOUND_SENSOR_PIN, INPUT);
  
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  delay(500);
  setColor(0, NUM_LEDS, 255,255,255);
  FastLED.show();
  delay(2000);
  setColor(0, NUM_LEDS, 0,0,0);
  FastLED.show();
  delay(1000);
}


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

//Mode 0 - Turns all LEDs off
void turnOff(){
  setColor(0, NUM_LEDS, 0,0,0);
  FastLED.show();
}

//Mode 2 - Sin Wave
void modeColorWave(int hue) {
  int curWaveRad = gWaveRad;

  gWaveRad += 0.01;

  for(int i = 0; i < NUM_LEDS; i+= 7){
    int val = (sin(curWaveRad) + 1) * 127;
    curWaveRad++;
    setColor(i, 7, hue, 255, val);
  }
  FastLED.show();
}

//Mode 4+5
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


//#########################################################



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
  gHue = net_values[1];
  gVal = net_values[2];
  gSat = net_values[3];
  gFourthVal = net_values[4];
  gFiftVal = net_values[5];
  gSixtVal = net_values[6];
}
