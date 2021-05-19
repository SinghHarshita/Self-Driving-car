const int EnableL = 5;
const int HighL = 6;     //Left Side Motors
const int LowL = 7;

const int EnableR = 10;
const int HighR = 8;    //Right Side Motors
const int LowR = 9;

// Arduino and RaspberryPi Connecting pins
//const int D0 = 0; // Rpi pin 21 LSB
//const int D1 = 1; // Rpi pin 22
//const int D2 = 2; // Rpi pin 23
//const int D3 = 3; // Rpi pin 24 MSB

//int a,b,c,d,data=0;
// Reading data received from Rpi

/*void Data(){
  a = digitalRead(D0);
  b = digitalRead(D1);
  c = digitalRead(D2);
  d = digitalRead(D3);

  data = 8*d+4*c+2*b+a;
}*/
 
void setup() {
  // put your setup code here, to run once:
  // Enabling the pins for receiving the output
  pinMode(EnableL,OUTPUT);
  pinMode(HighL,OUTPUT);
  pinMode(LowL,OUTPUT);

  pinMode(EnableR,OUTPUT);
  pinMode(HighR,OUTPUT);
  pinMode(LowR,OUTPUT);
 
  /*pinMode(D0,INPUT_PULLUP);
  pinMode(D1,INPUT_PULLUP);
  pinMode(D2,INPUT_PULLUP);
  pinMode(D3,INPUT_PULLUP);*/  
  // end method
}

void Forward(){
  digitalWrite(HighL,LOW);  //Code may change for our motor from low to high
  digitalWrite(LowL,HIGH);  // and vice versa
  analogWrite(EnableL,255);

  digitalWrite(HighR,LOW);  //Code may change for our motor from low to high
  digitalWrite(LowR,HIGH);  //and vice versa
  analogWrite(EnableR,255);
}


void Backward(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,255); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,255);
}

void Right1(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,255); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,200);
}

void Right2(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,255); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,160);
}

void Right3(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,255); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,100);
}


void Left1(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,200); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,255);
}


void Left2(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,160); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,255);
}

void Left3(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,100); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,255);
}

void Stop(){
  digitalWrite(HighL,HIGH);
  digitalWrite(LowL,LOW);   //Code may change for our motor from low to high 
  analogWrite(EnableL,0); //and vice versa

  digitalWrite(HighR,HIGH); //Code may change for our motor from low to high
  digitalWrite(LowR,LOW);   // and vice versa
  analogWrite(EnableR,0);
}

void loop() {
  // put your main code here, to run repeatedly:
  Forward();
  //Left1();
  //Right1();
  //Backward();
  //Data(); // data from Rpi

  // similarly for different scenarios, write commands

}
