#define PIN_VICON_INPUT   7
#define BAUD_RATE         115200
#define RECORD_START_KEY  's'
#define RECORD_STOP_KEY   'e'

int prevSensorValue;
int sensorValue;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(BAUD_RATE);

  pinMode(PIN_VICON_INPUT, INPUT);

  prevSensorValue = digitalRead(PIN_VICON_INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  sensorValue = digitalRead(PIN_VICON_INPUT);

  if (prevSensorValue == LOW && sensorValue == HIGH)
    Serial.write(RECORD_START_KEY); // start record
  else if (prevSensorValue == HIGH && sensorValue == LOW)
    Serial.write(RECORD_STOP_KEY); // end record

  prevSensorValue = sensorValue;
}
