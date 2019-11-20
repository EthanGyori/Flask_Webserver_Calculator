

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
const char *ssid = "SSID";
const char *password = "PASSWORD";
const int red = 15;
const int green = 12;
const int blue = 13;
void setup(void) {
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) ;
    delay(1000);
    Serial.print("Connecting. . .");
  }
}
void loop(void) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://192.168.11.102:4000/led");
    int httpCode = http.GET();
    String payload;
    if(httpCode > 0) {
      payload = http.getString();
    }
    Serial.print(payload);
    if(payload == "Ethan") {
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
      digitalWrite(red, HIGH);
    }
    else if (payload == "Max") {
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
      digitalWrite(blue, HIGH);
    }
    else if (payload == "Bryce") {
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
      digitalWrite(green, HIGH);
    }
    else {
      digitalWrite(red, LOW);
      digitalWrite(blue, LOW);
      digitalWrite(green, LOW);
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.print("Err. . . wrong payload");
    }
    http.end();
  }
}
