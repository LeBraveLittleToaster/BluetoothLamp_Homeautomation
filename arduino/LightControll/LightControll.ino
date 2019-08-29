int incomingByte = 0;

//MODE and 6 x 0-255 values
int net_values[] = {0,0,0,0,0,0,0};

int read_counter = 0;
int MAX_AMOUNT_READ = 7;

boolean isReading = true;
boolean isLightUpdateNeeded = false; 

void setup() {

  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  Serial.println("Hello Blue World");
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.read(); // read the incoming byte:
    delay(1);
    
    Serial.print("Received: ");
    Serial.println(incomingByte);
    
    if(incomingByte != -1){
      if(isReading && incomingByte != '#'){
        net_values[read_counter] = incomingByte;
        read_counter++;
        if(read_counter >= MAX_AMOUNT_READ){
          isReading = false;
          isLightUpdateNeeded = true;
          Serial.println("Finished reading");
        }
      }else if(incomingByte == '#'){
        read_counter = 0;
        isReading = true;
        Serial.println("Reading values");
      } else{
        Serial.println("Empty byte");
      }
    }
  }
  

  if(!isReading && isLightUpdateNeeded){
    Serial.println("VALUES START");
    Serial.print("| ");
    for(int i = 0; i < 7; i++){
      Serial.print(net_values[i]);
      Serial.print(" | ");
    }
    Serial.println(" (Count: 7) ");
    Serial.println("VALUES END");
    isLightUpdateNeeded = false;
  }
}
