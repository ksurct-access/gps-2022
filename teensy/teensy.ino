#include "src/Json.hpp"
#include "src/Gps.hpp"
#include "src/Sensors.hpp"

json::Data data;

void setup()
{
    Serial.begin(115200);
    sensorsInit();
    init();
    data.latitude = 90;
}

void loop()
{
    delay(10);
    gpsUpdate();
    if(isDataReady()){
        getGpsData(data);
    }
    collectSensorData(1, data);
    data.sendJson();
}
