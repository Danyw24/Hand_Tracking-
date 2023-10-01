  /*
    │ #        ____                            ___  __ __
    │ #       / __ \____ _____  __  ___      _|__ \/ // /
    │ #      / / / / __ `/ __ \/ / / / | /| / /_/ / // /_
    │ #     / /_/ / /_/ / / / / /_/ /| |/ |/ / __/__  __/
    │ #    /_____/\__,_/_/ /_/\__, / |__/|__/____/ /_/   
    │ #                      /____/                      
    │ #   Radio Car Side
    │ #   Author:Danyw24
    │ #   Github: https://github.com/Danyw24
    │ #   Description: RF data reciver in the rc car
    │ #   Version: Atmega328p and nrf24l01 V3
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

bool leftState = false;
bool rightState = false;
unsigned long lastLeftActivationTime = 0;
unsigned long lastRightActivationTime = 0;


DataStatus data;
unsigned long lastRecvTime = 0;

const uint64_t pipeIn = 0xE8E8F0F0E1LL;

RF24 radio(8, 10); //nRF24L01 (CE, CSN)


#define AdvancePin 9 // PB1
#define DownPin 7 // PD7
#define LeftPin 6 // PD6
#define RightPin 5 // PD5
#define LED_STATUS_PIN 4 //PD4

 
void setup() {
    //configCar();
    resetData();
    radio.begin();
    radio.setAutoAck(false);
    //radio.setPALevel(RF24_PA_MAX); 
    radio.setDataRate(RF24_250KBPS); 
    radio.openReadingPipe(1, pipeIn);
    radio.startListening();
}

void configCar(){
  pinMode(AdvancePin, OUTPUT);
  pinMode(DownPin, OUTPUT);
  pinMode(LeftPin, OUTPUT);
  pinMode(RightPin, OUTPUT); 
}


void loop() {
    recvData();
    unsigned long now = millis();
    if (now - lastRecvTime > 1000) {
        //Serial.println("Signal lost!");
        resetData();
    } 
}

void recvData() {
    while (radio.available()) {
        radio.read(&data, sizeof(DataStatus));
        writeDataCar();
        lastRecvTime = millis(); 
    }
}

void writeDataCar(){
  if(data.up){
    digitalWrite(AdvancePin, HIGH);
    delay(500);
  }else{
    digitalWrite(AdvancePin, LOW);
  }

  if(data.left){
    if(!leftState){
    digitalWrite(LeftPin, HIGH);
    leftState = true;
    }
    else{
    digitalWrite(LeftPin, LOW);
    leftState= false;}
  }

  if(data.right){
    if(!rightState){
    digitalWrite(RightPin, HIGH);
    rightState = true;
    }else{
    digitalWrite(RightPin, LOW);
    rightState = false;}
  }

  if(data.down){
    digitalWrite(DownPin, HIGH);
    delay(500);
  }else{
    digitalWrite(DownPin, LOW);
  }
  resetData();
}

void resetData(){
  data.up = false;
  data.down = false;
  data.left = false;
  data.right = false;
}