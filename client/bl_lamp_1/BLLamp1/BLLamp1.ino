char msgBuf[3];

void setup() {
  Serial.begin(9600);
  Serial.println("Hello world");
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    if(c == '#'){
      Serial.println("New Message");
      Serial.readBytes(msgBuf, 3);
      Serial.print("V=");
      Serial.println(msgBuf);
    }
  }

}
