  /*
    │ #        ____                            ___  __ __
    │ #       / __ \____ _____  __  ___      _|__ \/ // /
    │ #      / / / / __ `/ __ \/ / / / | /| / /_/ / // /_
    │ #     / /_/ / /_/ / / / / /_/ /| |/ |/ / __/__  __/
    │ #    /_____/\__,_/_/ /_/\__, / |__/|__/____/ /_/   
    │ #                      /____/                      
    │ #   Radio Transmitter
    │ #   Author:Danyw24
    │ #   Github: https://github.com/Danyw24
    │ #   Description: RF data transmiter to the rc car
    │ #   Version: Arduino uno and nrf24l01 V3
    │ #   OS: Fedora 37
    │ 
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

struct DataStatus{
byte up;
byte down;
byte left;
byte right;
};

DataStatus data;

const uint64_t pipeOut = 0xE8E8F0F0E1LL;

RF24 radio(8, 10); //nRF24L01 (CE, CSN)

void setup() {
    Serial.begin(9600);
    radio.begin();
    radio.setAutoAck(false);
    radio.setPALevel(RF24_PA_MAX);
    radio.setDataRate(RF24_250KBPS); 
    radio.openWritingPipe(pipeOut);
    resetData();
}

void loop() {
  if (Serial.available() != 0){
    String stringData = Serial.readStringUntil('\n');
    if(strcmp(stringData.c_str(), "up") == 0){
      data.up = true;}
    else if(strcmp(stringData.c_str(), "down") == 0){
      data.down = true;}
    else if(strcmp(stringData.c_str(), "left") == 0){
      data.left = true;}
    else if (strcmp(stringData.c_str(), "right") == 0){
      data.right = true;}
  }
  radio.write(&data, sizeof(data));
  resetData();
}

void resetData(){
  data.up = false;
  data.down = false;
  data.left = false;
  data.right = false;
}