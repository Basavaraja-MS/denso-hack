char *result = malloc(5);
char *result1 = malloc(5);
char *result2 = malloc(5);

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

        int t1= analogRead(A0);
        sprintf(result, "%04d", t1);
        Serial.print(result);
        Serial.print(" ");

        int t2= analogRead(A1);
        sprintf(result1, "%04d", t2);
        Serial.print(result1);
        Serial.print(" ");

        int t3= analogRead(A2);
        sprintf(result2, "%04d\n", t3);
        Serial.print(result2);
        delay(100);
}
