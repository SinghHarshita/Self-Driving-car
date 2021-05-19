const int EnableL = 5;
const int HighL = 6;     //Left Side Motors
const int LowL = 7;

const int EnableR = 10;
const int HighR = 8;    //Right Side Motors
const int LowR = 9;


void setup() {
  // put your setup code here, to run once:
  pinMode(EnableL,OUTPUT);
  pinMode(HighL,OUTPUT);
  pinMode(LowL,OUTPUT);

  pinMode(EnableR,OUTPUT);
  pinMode(HighR,OUTPUT);
  pinMode(LowR,OUTPUT);
};

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


void loop() {
  // put your main code here, to run repeatedly:
  Forward();
}
