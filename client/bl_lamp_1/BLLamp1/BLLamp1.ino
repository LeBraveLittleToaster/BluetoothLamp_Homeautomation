int r = 0;
int g = 0;
int b = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Hello world");
}

void loop() {
  while(Serial.available()){
    delay(10);
    char c = Serial.read();
    if(c == '#'){
      r = readValue(4);
      g = readValue(4);
      b = readValue(4);
    }
  }
}

int readValue(int width){
  Serial.println("Start reading");
  int v = 0;
  int m = width - 1;
  for(int i = 0; i < width; i++){
    if(m > 0){
      v = v + (Serial.parseInt() * pow(10, m));
    }else{
      v = v + Serial.parseInt();
    }
    m--;
  }
  Serial.print("Stopped reading, v is ");
  Serial.println(v);
  return v;
}
