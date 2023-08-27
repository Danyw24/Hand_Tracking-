#include <SPI.h>
#include <RH_NRF24.h>

RH_NRF24 radio (9,10);

void setup() {
 Serial.begin(9600);
 if(! radio.init()){
    Serial.println("[-] Error al iniciar el remoto");
 }
 Serial.println("[+] Remoto iniciado.");
 radio.setChannel(1);
 radio.setRF(RH_NRF24::DataRate2Mbps, RH_NRF24::TransmitPower0dBm);
}

void loop() {
  if(radio.available()){
    uint8_t buf [32];
    uint8_t len = sizeof(buf);
    if(radio.recv(buf, &len)){
      buf[len] = '\0';
      Serial.println((char*)buf);
    }
  }
  
}
