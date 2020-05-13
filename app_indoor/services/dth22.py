import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


class DTH22():
    def __init__(self):
        self.DTH_PIN = 4
        self.DHT_SENSOR = Adafruit_DHT.DHT22

    def read_values(self, save=False, path=None):
        if save:
            f = open('/home/pi/humidity.csv', 'a+')
            if os.stat('/home/pi/humidity.csv').st_size == 0:
                    f.write('Date,Time,Temperature,Humidity\r\n')
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None and save:
            f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        elif humidity is not None and temperature is not None and not save:
            print(f"{time.strftime('%m/%d/%y')}, {time.strftime('%H:%M')}")
            print(f"temperature: {temperature} \n humidity: {humidity}")
        else:
            print("Failed to retrieve data from humidity sensor")
            return temperature, humidity





# try:
#     f = open('/home/pi/humidity.csv', 'a+')
#     if os.stat('/home/pi/humidity.csv').st_size == 0:
#             f.write('Date,Time,Temperature,Humidity\r\n')
# except:
#     pass

# while True:
#     humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

#     if humidity is not None and temperature is not None:
#         f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
#     else:
#         print("Failed to retrieve data from humidity sensor")

#     time.sleep(30)