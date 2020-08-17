
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.read()==1){
    for(int i=0;i<10;i++){
      for(int j=0;j<10;j++){
        for(int k=0;k<10;k++){
          Serial.print(i);
          Serial.print(' ');
          Serial.print(j);
          Serial.print(' ');
          Serial.println(k);
          delay(100);
        
        }
      }
     }
  }

}
