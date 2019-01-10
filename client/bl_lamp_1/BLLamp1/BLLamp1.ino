int length = 12;

void setup() {
  Serial.begin(9600);
  Serial.println("Hello world");
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    if(c == '#'){
      char msgBuf[length];
      Serial.println("New Message");
      Serial.readBytes(msgBuf, length);
      Serial.print("V=");
      Serial.println(msgBuf);
      int v = 0;
      for(int i = 0; i < sizeof(msgBuf); i++){
        v = (int) msgBuf[i];
        Serial.print(v);
      }
    }
  }

}
