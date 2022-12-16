int DL=1000;

long Speed;
long Rpm;
long Volts;
long current;
long motor;
long acc;

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  Speed = random(100);
  Rpm=random(1000,5000);
  Volts=random(200,300);
  current=random(200,300);
  motor=random(90,100);
  acc=random(80,90);
  Serial.print(Speed);
  Serial.print(",");
  Serial.print(Rpm);
  Serial.print(",");
  Serial.print(Volts);
  Serial.print(",");
  Serial.print(current);
  Serial.print(",");
  Serial.print(motor);
  Serial.print(",");
  Serial.println(acc);

  delay(100);
}