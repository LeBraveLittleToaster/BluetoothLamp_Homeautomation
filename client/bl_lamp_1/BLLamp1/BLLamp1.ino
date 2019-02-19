#include <FastLED.h>

// How many leds in your strip?
#define NUM_LEDS 32

// For led chips like Neopixels, which have a data line, ground, and power, you just
// need to define DATA_PIN.  For led chipsets that are SPI based (four wires - data, clock,
// ground, and power), like the LPD8806 define both DATA_PIN and CLOCK_PIN
#define DATA_PIN 4

// Define the array of leds
CRGB leds[NUM_LEDS];


void setup() {
  digitalWrite(LED_BUILTIN, LOW);
  Serial.begin(9600);
  Serial.println("Hello world");
  //FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);
  delay(2000);
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    if(c == '#'){
      int r = readValue();
      Serial.print("r=");
      Serial.println(r);
      int g = readValue();
      Serial.print("g=");
      Serial.println(g);
      int b = readValue();
      Serial.print("b=");
      Serial.println(b);
      int m = readValue();
      Serial.print("m=");
      Serial.println(m);
      //runColorByMode(r,g,b,m);
    }
    if(c == 'X'){
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write("quit");
    }
  }
  /*
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  runColorByMode(255,0,0,0);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  runColorByMode(0,0,255,0);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  runColorByMode(0,255,0,0);
  */
}
int readValue(){
  Serial.print("START_");
  int x1 = (Serial.read() - 48) * 1000 ;
  delay(1);
  Serial.print(x1);
  Serial.print("_");
  int x2 = (Serial.read() - 48 ) * 100;
  delay(1);
  Serial.print(x2);
  Serial.print("_");
  int x3 = (Serial.read() - 48) * 10;
  delay(1);
  Serial.print(x3);
  Serial.print("_");
  int x4 = Serial.read() - 48;
  delay(1);
  Serial.print(x4);
  Serial.println("_END");
  return x1 + x2 + x3 + x4;
}

void runColorByMode(int r, int g, int b, int mode){
  for(int i = 0; i < NUM_LEDS; i++){
    leds[i].red = r;
    leds[i].green = g;
    leds[i].blue = b;
  }
  FastLED.show();
}
