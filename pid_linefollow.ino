
const int left2 = A0;
const int left1 = A1;
const int center = A2;
const int right1 = A3;
const int right2 = A4;

// Motor 1
int pinAIN1 = 5; // Direction
int pinAIN2 = 4; // Direction
int pinPWMA = 3; // Speed

// Motor 2
int pinBIN1 = 7; // Direction
int pinBIN2 = 8; // Direction
int pinPWMB = 9; // Speed

// Standby
int pinSTBY = 6;

// PD Controller Parameters
float Kp = 20;   // Proportional gain (adjust based on testing)
float Kd = 15;   // Derivative gain (adjust based on testing)
int baseSpeed = 150; // Base motor speed (0-255)

int lastError = 0;
unsigned long lastTime = 0;

void setup() {
  // Set the PIN Modes
  pinMode(pinPWMA, OUTPUT);
  pinMode(pinAIN1, OUTPUT);
  pinMode(pinAIN2, OUTPUT);

  pinMode(pinPWMB, OUTPUT);
  pinMode(pinBIN1, OUTPUT);
  pinMode(pinBIN2, OUTPUT);

  pinMode(pinSTBY, OUTPUT);

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  
  Serial.begin(9600);
  digitalWrite(pinSTBY, HIGH);
}

void loop() {
  // Read sensor values
  int sLeft2 = analogRead(left2);
  int sLeft1 = analogRead(left1);
  int sCenter = analogRead(center);
  int sRight1 = analogRead(right1);
  int sRight2 = analogRead(right2);

  // Calculate position error (-2 to +2 scale)
  int error = 0;
  int sensorSum = sLeft2 + sLeft1 + sCenter + sRight1 + sRight2;

  if (sensorSum != 0) {
    // Weighted average to determine line position
    error = (-2 * sLeft2) + (-1 * sLeft1) + (0 * sCenter) + (1 * sRight1) + (2 * sRight2);
  } else {
    // No line detected - use last error or stop
    // This could be enhanced with a "lost line" recovery strategy
    motorLeft(0);
    motorRight(0);
    return;
  }

  // Calculate time difference for derivative term
  unsigned long currentTime = millis();
  float deltaTime = (currentTime - lastTime) / 1000.0; // Convert to seconds
  lastTime = currentTime;

  // Calculate derivative (change in error)
  int derivative = (error - lastError) / deltaTime;
  lastError = error;

  // Calculate PD output
  int pdOutput = Kp * error + Kd * derivative;

  // Adjust motor speeds based on PD output
  int leftSpeed = baseSpeed - pdOutput;
  int rightSpeed = baseSpeed + pdOutput;

  // Constrain speeds to valid range (0-255)
  leftSpeed = constrain(leftSpeed, 0, 255);
  rightSpeed = constrain(rightSpeed, 0, 255);

  // Apply motor speeds
  motorLeft(leftSpeed);
  motorRight(rightSpeed);

  // Optional: Print debug information
  Serial.print("Error: ");
  Serial.print(error);
  Serial.print(" PD Out: ");
  Serial.print(pdOutput);
  Serial.print(" Left: ");
  Serial.print(leftSpeed);
  Serial.print(" Right: ");
  Serial.println(rightSpeed);

  delay(10); // Small delay to prevent overwhelming the serial monitor
}

void motorRight(int speed) {
  digitalWrite(pinAIN1, LOW);
  digitalWrite(pinAIN2, HIGH);
  analogWrite(pinPWMA, speed);
}

void motorLeft(int speed) {
  digitalWrite(pinBIN1, HIGH);
  digitalWrite(pinBIN2, LOW);
  analogWrite(pinPWMB, speed);
}