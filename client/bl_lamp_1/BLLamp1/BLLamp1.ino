int length = 12;
int numberLength = 4;
int numberCount = 3;

void setup() {
  Serial.begin(9600);
  Serial.println("Hello world");
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    if(c == '#'){
      /*
      char msgBuf[length];
      Serial.println("New Message");
      Serial.readBytes(msgBuf, length);
      Serial.print("V=");
      Serial.println(msgBuf);
      */
      for(int i = 0; i < numberCount; i++){
        int r = readValue();
        Serial.println(r);
        int g = readValue();
        Serial.println(g);
        int b = readValue();
        Serial.println(b);
      }
    }
  }
}
int readValue(){
  Serial.print("START_");
  int x1 = 48 - Serial.read();
  Serial.print(x1);
  Serial.print("_");
  int x2 = 48 - Serial.read();
  Serial.print(x2);
  Serial.print("_");
  int x3 = 48 - Serial.read();
  Serial.print(x3);
  Serial.print("_");
  int x4 = 48 - Serial.read();
  Serial.print(x4);
  Serial.println("_END");
  return x1 + x2 + x3 + x4;
}
