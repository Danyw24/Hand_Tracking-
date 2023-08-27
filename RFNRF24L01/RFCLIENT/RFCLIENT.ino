#include<SPI.h>
#include <RH_NRF24.h>

RH_NRF24 radio;

void setup() { 
  Serial.begin(9600);
  configRF();
}

void loop() {
  // Data sending   
   uint8_t data[] = "Data from client";
   Serial.println("[+]Sending data...");
   radio.send(data, sizeof(data)); 
   Serial.println("[+]Data Sended.");
}


void configRF(){
  if(!radio.init())
    Serial.println("[!] Init Error");
  if(!radio.setChannel(2))
    Serial.println("[!] Channel Error");
  if(!radio.setRF(RH_NRF24::DataRate250kbps, RH_NRF24::TransmitPower0dBm))
    Serial.println("[!] Setting RF Error");
  else 
     Serial.println("[+] RF started succesfully");
}
