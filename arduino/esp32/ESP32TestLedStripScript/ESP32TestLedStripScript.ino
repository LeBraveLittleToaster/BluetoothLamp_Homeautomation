#include <FastLED.h>
#include "credentials.h"
#include "EspMQTTClient.h"

#define NUM_LEDS 3
#define DATA_PIN 12 //D12

EspMQTTClient client(
  WIFI_SSID,
  WIFI_PASSWD,
  MQTT_SERVER,
  MQTT_USERNAME,
  MQTT_PASSWORD,
  "MyEsp",
  MQTT_PORT
);

uint8_t gHue = 0;
uint8_t gBrightness = 255;
uint8_t  gHueDelta = 3;


CRGB leds[NUM_LEDS];


void setup() {

  Serial.begin(9600);

  
  Serial.println("LED controller coming online...");
  Serial.println(WIFI_SSID);

  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(gBrightness);
  delay(500);
  setColor(0, NUM_LEDS, 255, 255, 255);
  FastLED.show();
  delay(2000);
  setColor(0, NUM_LEDS, 0, 0, 0);
  FastLED.show();
  delay(1000);
}


void onConnectionEstablished() {
  client.subscribe("test/in", [] (const String &payload)  {
    Serial.println(payload);
  });

  client.publish("test/out", "This is a message from myesp");
}


  


void loop() {
  client.loop();
  
  setColor(0, NUM_LEDS, gHue, 255, 255);
  delay(100);
  FastLED.show();
}

void setColor(int offset, int count, int hue, int sat, int value) {
  for (int i = offset; i < offset + count; i++) {
    leds[i] = CHSV(hue, sat, value);
  }
}
