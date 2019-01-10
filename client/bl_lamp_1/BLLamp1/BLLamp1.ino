void setup() {
  Serial.begin(9600);
  Serial.println("Hello world");
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    Serial.print(c);
  }

}
