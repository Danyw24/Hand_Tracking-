/*
#        ____                            ___  __ __
#       / __ \____ _____  __  ___      _|__ \/ // /
#      / / / / __ `/ __ \/ / / / | /| / /_/ / // /_
#     / /_/ / /_/ / / / / /_/ /| |/ |/ / __/__  __/
#    /_____/\__,_/_/ /_/\__, / |__/|__/____/ /_/   
#                      /____/                      
#   Radio Car Side
#   Author:Danyw24
#   Github: https://github.com/Danyw24
#   Description: RF data reciver in the rc car
#   Version: esp32 and nrf24l01 V3
#   OS: Fedora 3

#
#   DIAGRAM
#   
ESP32                  NRF24L01
--------------------   --------------------
GPIO18 (SCK)   ---------- SCK
GPIO23 (MOSI)  ---------- MOSI
GPIO19 (MISO)  ---------- MISO
GPIO5  (CSN)   ---------- CSN
GPIO17 (CE)    ---------- CE
3.3V           ---------- VCC
GND            ---------- GND

*/
#define SCK_PIN   18 // GPIO18 (SCK)
#define MOSI_PIN  23 // GPIO23 (MOSI)
#define MISO_PIN  19 // GPIO19 (MISO)
#define CSN_PIN   27 // GPIO5 (CSN)
#define CE_PIN    26 // GPIO17 (CE)


#include <SPI.h>
#include <RH_NRF24.h>

#define AdvancePin 16 // D8
#define BackPin 15 // D3
#define LeftPin 2 // D4
#define RightPin 0 // D0

bool LeftState, RightState;

RH_NRF24 radio(14,12);

void setup() 
{
  Serial.begin(9600);
  configCar();
  configRF();
}

void loop()
{
  if (radio.available())
  {
    uint8_t buf[RH_NRF24_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);
    if (radio.recv(buf, &len))
    {
      Serial.print("[+]Request: ");
      Serial.println((char*)buf);
      moveRCCarFromString((char*)buf);
    }
    else
    {
      Serial.println("recv failed");
    }
  }
}

void configRF(){
  bool success = true;
  if(!radio.init()){
    Serial.println("[!] Init Error");
    success = false;}
  if(!radio.setChannel(2)){
    Serial.println("[!] Channel Error");
    success = false;}
  if(!radio.setRF(RH_NRF24::DataRate250kbps, RH_NRF24::TransmitPower0dBm)){
    Serial.println("[!] Setting RF Error");
    success = false;}
  if(success){
    Serial.println("[+] RF started succesfully");}
}


void configCar(){
  pinMode(AdvancePin, OUTPUT);
  pinMode(BackPin, OUTPUT);
  pinMode(LeftPin, OUTPUT);
  pinMode(RightPin, OUTPUT);
  
}

void moveRCCarFromString (char * instruction ){

  if(strcmp(instruction, "UP") == 0){
    digitalWrite(AdvancePin, HIGH);
    delay(1000);
    digitalWrite(AdvancePin, LOW);
  }

  if(strcmp(instruction, "BACK") == 0){
    digitalWrite(BackPin, HIGH);
    delay(1000);
    digitalWrite(BackPin, LOW);
  }
  
  if(strcmp(instruction, "LEFT") == 0){
    if(!LeftState){
      digitalWrite(LeftPin, HIGH);
      LeftState = true;
    }else{
      digitalWrite(LeftPin, LOW);
      LeftState = false;
    }
  }

  if(strcmp(instruction, "RIGHT") == 0){
    if(!RightState){
      digitalWrite(RightPin, HIGH);
      RightState = true;
    }else{
      digitalWrite(RightPin, LOW);
      RightState = false;
    }
  }
  
}
