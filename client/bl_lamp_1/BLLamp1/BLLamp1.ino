void setup() {
  Serial.begin(9600);
  Serial.println("Hello world");
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    int i = (int)c;
    Serial.print("| C=");
    Serial.print(c);
    Serial.print(" | I=");
    Serial.println(i);
  }

}
