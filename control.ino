const int pin1 = 2;
const int pin2 = 3;
const int pin3 = 4;
const int pin4 = 5;
const int pin5 = 6;
const int pin6 = 7;
const int pin7 = 8;
const int pin8 = 9;
const int pin9 = 10;
const int pin10 = 11;
const int pin13 = 13;
int pression_analogique_1 = 0;
int pression_analogique_2 = 0;
float pression_numerique_1 = 0;
float pression_numerique_2 = 0;
int commande=0;

void setup()
{
 pinMode(pin1,OUTPUT);
 pinMode(pin2,OUTPUT);
 pinMode(pin3,OUTPUT);
 pinMode(pin4,OUTPUT);
 pinMode(pin5,OUTPUT);
 pinMode(pin6,OUTPUT);
 pinMode(pin7,OUTPUT);
 pinMode(pin8,OUTPUT);
 pinMode(pin9,OUTPUT);
 pinMode(pin10,OUTPUT);
 pinMode(pin13,OUTPUT);
 Serial.begin(9600);
}
void loop()
{
 if (Serial.available()) 
 {
 
 commande = Serial.parseInt();
 switch (commande){
  case 1 :
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  digitalWrite(pin5,HIGH);
  digitalWrite(pin6,LOW);
  digitalWrite(pin7,LOW);
  digitalWrite(pin8,LOW);
  digitalWrite(pin9,LOW);
  digitalWrite(pin10,LOW);
  Serial.flush();
  break;
  case 2 :
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  digitalWrite(pin5,LOW);
  digitalWrite(pin6,HIGH);
  digitalWrite(pin7,LOW);
  digitalWrite(pin8,LOW);
  digitalWrite(pin9,LOW);
  digitalWrite(pin10,LOW);
  Serial.flush();
  break;
  case 3 :
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  digitalWrite(pin5,LOW);
  digitalWrite(pin6,LOW);
  digitalWrite(pin7,LOW);
  digitalWrite(pin8,HIGH);
  digitalWrite(pin9,LOW);
  digitalWrite(pin10,LOW);
  Serial.flush();
  break;
  case 4:
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  digitalWrite(pin5,LOW);
  digitalWrite(pin6,LOW);
  digitalWrite(pin7,HIGH);
  digitalWrite(pin8,LOW);
  digitalWrite(pin9,LOW);
  digitalWrite(pin10,LOW);
  Serial.flush();
  break;
  case 5:
  digitalWrite(pin1,HIGH);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,HIGH);
  digitalWrite(pin4,HIGH);
  digitalWrite(pin5,LOW);
  digitalWrite(pin6,LOW);
  digitalWrite(pin7,LOW);
  digitalWrite(pin8,LOW);
  digitalWrite(pin9,LOW);
  digitalWrite(pin10,LOW);
  Serial.flush();
  break;
  case 6:
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,LOW);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  digitalWrite(pin5,LOW);
  digitalWrite(pin6,LOW);
  digitalWrite(pin7,LOW);
  digitalWrite(pin8,LOW);
  digitalWrite(pin9,LOW);
  digitalWrite(pin10,HIGH);
  Serial.flush();
  break;
  case 7:
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,HIGH);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  digitalWrite(pin5,LOW);
  digitalWrite(pin6,LOW);
  digitalWrite(pin7,LOW);
  digitalWrite(pin8,LOW);
  digitalWrite(pin9,HIGH);
  digitalWrite(pin10,LOW);
  Serial.flush();
  break;
  case 8 :
  pression_analogique_1 = analogRead(A0);
  
  break;
  case 9 :
  pression_analogique_2 = analogRead(A1);
  
  break;
  default :
  digitalWrite(pin1,LOW);
  digitalWrite(pin2,LOW);
  digitalWrite(pin3,LOW);
  digitalWrite(pin4,LOW);
  digitalWrite(pin5,LOW);
  digitalWrite(pin6,LOW);
  digitalWrite(pin7,LOW);
  digitalWrite(pin8,LOW);
  digitalWrite(pin9,LOW);
  digitalWrite(pin10,LOW);
  Serial.flush();
  break;
  
 }
 }
 Serial.flush(); 
} 
