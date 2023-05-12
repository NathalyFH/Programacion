#include <Servo.h>

Servo motor1; // DECLARAR SERVO 1

int PINSERVO = 2; // PIN DIGITAL PWM 3 DONDE ESTÁ CONECTADO EL SERVO 1
int PULSOMIN = 1000; // PULSO MÍNIMO PARA 0°
int PULSOMAX = 2000; // PULSO MÁXIMO PARA 180°

void setup() { 
motor1.attach (PINSERVO, PULSOMIN, PULSOMAX); // PERMITIRÁ INICIALIZAR EL SERVO CON LOS VALORES DADOS
}

void loop() {

motor1.write (0); // ENVIAR LOS GRADOS AL SERVO 1
delay(1000);  // ESPERA 1 SEGUNDO EN LA POSICIÓN FIJADA

motor1.write (6); 
delay(1000);

motor1.write (12);
delay(1000);

motor1.write (18); 
delay(1000);

motor1.write (24); 
delay(1000);

motor1.write (30); 
delay(1000);

motor1.write (36); 
delay(1000);

motor1.write (42);
delay(1000);

motor1.write (48); 
delay(1000);

motor1.write (54); 
delay(1000);

motor1.write (60); 
delay(1000);

motor1.write (66); 
delay(1000);

motor1.write (72);
delay(1000);

motor1.write (78); 
delay(1000);

motor1.write (84); 
delay(1000);

motor1.write (90); 
delay(1000);

motor1.write (96); 
delay(1000);

motor1.write (102);
delay(1000);

motor1.write (108); 
delay(1000);

motor1.write (114); 
delay(1000);

motor1.write (120); 
delay(1000);

motor1.write (126); 
delay(1000);

motor1.write (132);
delay(1000);

motor1.write (138); 
delay(1000);

motor1.write (144); 
delay(1000);

motor1.write (150); 
delay(1000);

motor1.write (156); 
delay(1000);

motor1.write (162);
delay(1000);

motor1.write (168); 
delay(1000);

motor1.write (174); 
delay(1000);

motor1.write (180); 
delay(1000);

motor1.write (174);
delay(1000);

motor1.write (168); 
delay(1000);

motor1.write (162);
delay(1000);

motor1.write (156); 
delay(1000);

motor1.write (150); 
delay(1000);

motor1.write (144); 
delay(1000);

motor1.write (138); 
delay(1000);

motor1.write (132);
delay(1000);

motor1.write (126); 
delay(1000);

motor1.write (120); 
delay(1000);

motor1.write (114); 
delay(1000);

motor1.write (108); 
delay(1000);

motor1.write (102);
delay(1000);

motor1.write (96); 
delay(1000);

motor1.write (90); 
delay(1000);

motor1.write (84); 
delay(1000);

motor1.write (78); 
delay(1000);

motor1.write (72);
delay(1000);

motor1.write (66); 
delay(1000);

motor1.write (60); 
delay(1000);

motor1.write (54); 
delay(1000);

motor1.write (48); 
delay(1000);

motor1.write (42);
delay(1000);

motor1.write (36); 
delay(1000);

motor1.write (30); 
delay(1000);

motor1.write (24); 
delay(1000);

motor1.write (18); 
delay(1000);

motor1.write (12);
delay(1000);

motor1.write (6); 
delay(1000);
}
