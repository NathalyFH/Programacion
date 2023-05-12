#include <AFMotor.h>
AF_DCMotor motor1 (1);
AF_DCMotor motor2 (2);

void setup()
{
  motor1.setSpeed(250);
  motor2.setSpeed(250);
}

void loop()
{
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
}
