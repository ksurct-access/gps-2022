import serial
import json

class SerialInput(object):
    
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0')
        self.ser.flush()
        self.fr_data = ""
        self.fl_data = ""
        self.f_data = ""
        self.l_data = ""
        self.r_data = ""
        self.course = ""
        self.longitude = ""
        self.latitude = ""
        self.altitude = ""
        self.speed = ""

    def receiveData(self):
        if self.ser.in_waiting > 0:
            line = json.loads(self.ser.readline().decode('utf-8').rstrip())
            print(line)
            self.fr_data = line['fr_data']
            self.fl_data = line['fl_data']
            self.f_data = line['f_data']
            self.l_data = line['l_data']
            self.r_data = line['r_data']
            self.longitude = line['longitude']
            self.latitude = line['latitude']
            self.altitude = line['altitude']
            self.course = line['course']
        
    def getFrontRightSensorData(self):
        return self.fr_data
        
    def getFrontLeftSensorData(self):
        return self.fl_data
        
    def getFrontSensorData(self):
        return self.f_data
        
    def getLeftSensorData(self):
        return self.l_data
        
    def getRightSensorData(self):
        return self.r_data
        
    def getLongitude(self):
        return self.longitude
        
    def getLatitude(self):
        return self.latitude
        
    def getAltitude(self):
        return self.altitude
        
    def getCourse(self):
        return self.course

if __name__ == '__main__':
    # ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    # ser.flush()
    var = SerialInput()
    var.receiveData()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
