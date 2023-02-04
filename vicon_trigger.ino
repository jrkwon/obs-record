enum {
  BR_9600, BR_14400, BR_19200, BR_28800, BR_31250, BR_38400, BR_57600, BR_115200 
};

#define PIN_VICON_INPUT   7
#define BAUD_RATE_IDX     BR_115200
#define RECORD_START_KEY  's'
#define RECORD_STOP_KEY   'e'

int prevSensorValue;
int sensorValue;
unsigned long baudrates[] = { 9600ul, 14400ul, 19200ul, 28800ul, 31250ul, 38400ul, 57600ul, 115200ul };

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 115200 bits per second:
  Serial.begin(baudrates[BAUD_RATE_IDX]);

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
