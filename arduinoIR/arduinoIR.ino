#include <IRremote.h>

IRsend irsend;

#define CMD_BITS_SIZE     20u
#define CMD_SHUTTER       0xB4B8F
#define CMD_VIDEO         0x12B8F
#define CMD_DISP_BUTTON   0x28B8F
#define CMD_MENU          0x1CB8F
#define CMD_ZOOM_IN       0x52B8F
#define CMD_ZOOM_OUT      0xD2B8F

void setup()
{
  pinMode(2, INPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  if(!digitalRead(2)){
    digitalWrite(13, HIGH);
    for (int i = 0; i < 3; i++) {
		irsend.sendSony(CMD_MENU, CMD_BITS_SIZE);
		delay(40);
    }
    delay(50); //5 second delay between each signal burst
  }
  else {
    digitalWrite(13, LOW);
  }
}