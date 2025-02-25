#include <WiFi.h>            
#include "time.h"            

const char* ssid     = "Pichaya";    
const char* password = "somsomsomsom"; 

const char* ntpServer = "time.google.com";  
const long  gmtOffset_sec = 7 * 3600;    // เปลี่ยนเป็น GMT+7 (ประเทศไทย)
const int   daylightOffset_sec = 0;    

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    Serial.print("Connecting to WiFi");
    int timeout = 20; 
    while (WiFi.status() != WL_CONNECTED && timeout > 0) {
        delay(1000);
        Serial.print(".");
        timeout--;
    }

    if (WiFi.status() == WL_CONNECTED) {
        Serial.println("\nWiFi Connected!");
    } else {
        Serial.println("\nWiFi Connection Failed!");
        return;
    }

    configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);

    struct tm timeinfo;
    int retry = 10; 
    while (!getLocalTime(&timeinfo) && retry > 0) {
        Serial.println("Retrying NTP...");
        delay(2000);
        retry--;
    }

    if (retry == 0) {
        Serial.println("Failed to obtain time");
    } else {
        Serial.println("Time synchronized!");
    }
}

void loop() {
    struct tm timeinfo;
    if (getLocalTime(&timeinfo)) {
        Serial.printf("Current date & time in Thailand: %02d-%02d-%04d %02d:%02d:%02d\n", 
                      timeinfo.tm_mday, timeinfo.tm_mon + 1, timeinfo.tm_year + 1900, 
                      timeinfo.tm_hour, timeinfo.tm_min, timeinfo.tm_sec);
    } else {
        Serial.println("Error getting time!");
    }
    delay(1000);
}
