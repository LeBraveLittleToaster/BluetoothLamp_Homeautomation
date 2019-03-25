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
  Serial.println("LED controller coming online...");
  //FastLED.addLeds<WS2812B, DATA_PIN, RGB>(leds, NUM_LEDS);
  delay(2000);
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    if(c == '#'){
      int h = readColor();
      int s = readColor();
      int v = readColor();
      int m = Serial.read();
      Serial.println("+++++++++");
      Serial.println(h);
      Serial.println(s);
      Serial.println(v);
      Serial.println(m);
      Serial.println("+++++++++");
      delay(2000);
      //runColorByMode(r,g,b,m);
    }
  }
}

int readColor(){
  return Serial.read() * 2 % 255;
}

void runColorByMode(int r, int g, int b, int mode){
  for(int i = 0; i < NUM_LEDS; i++){
    leds[i].red = r;
    leds[i].green = g;
    leds[i].blue = b;
  }
  FastLED.show();
}
