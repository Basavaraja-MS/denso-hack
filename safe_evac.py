#import urllib.request as urllib2
import urllib2 
import spidev
import time
import os
import RPi.GPIO as GPIO  
from time import sleep  
class LCDDATA:  
  
    def __init__(self, pin_rs=12, pin_e=16, pins_db=[25, 24, 23, 18]):  
  
        self.pin_rs=pin_rs  
        self.pin_e=pin_e  
        self.pins_db=pins_db  
  
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)  
        GPIO.setup(self.pin_e, GPIO.OUT)  
        GPIO.setup(self.pin_rs, GPIO.OUT)  
        for pin in self.pins_db:  
            GPIO.setup(pin, GPIO.OUT)  
  
        self.clear()  
  
    def clear(self):  
        """ Blank / Reset LCD """  
  
        self.cmd(0x33)  
        self.cmd(0x32)  
        self.cmd(0x28)  
        self.cmd(0x0C)  
        self.cmd(0x06) 
        self.cmd(0x01) 
  
    def cmd(self, bits, char_mode=False):  
        """ Send command to LCD """  
  
        sleep(0.001)  
        bits=bin(bits)[2:].zfill(8)  
  
        GPIO.output(self.pin_rs, char_mode)  
  
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i], True)  
  
        GPIO.output(self.pin_e, True)  
        GPIO.output(self.pin_e, False)  
  
        for pin in self.pins_db:  
            GPIO.output(pin, False)  
  
        for i in range(4,8):  
            if bits[i] == "1":  
                GPIO.output(self.pins_db[::-1][i-4], True)  
  
  
        GPIO.output(self.pin_e, True)  
        GPIO.output(self.pin_e, False)  
  
    def message(self, text):  
        """ Send string to LCD. Newline wraps to second line"""  
  
        for char in text:  
            if char == '\n':  
                self.cmd(0xC0) # next line  
            else:  
                self.cmd(ord(char),True)  
  
if __name__ == '__main__':  
  
    lcd = LCDDATA()  
  


 
# Define delay between readings
"""
delay = 2
 
while True:
 
  lcd.cmd(0x80)
  lcd.message("Denso Project     ")
  lcd.cmd(0xC0)
  lcd.message("         Demo!")
 
 
  # Wait before repeating loop
  time.sleep(delay)
"""

def lcd_display (str, next_line):
    if next_line == 0:
        lcd.cmd(0x1)
        lcd.cmd(0x80)
        lcd.message(str)
    else:
       lcd.cmd(0xC0)
       lcd.message(str)

import serial
import time
import requests

z1baudrate = 9600
z1port = '/dev/ttyACM0'
sen_left = 0
sen_right = 0
sen_front = 0
i = 0
AVG_VAL = 10
timer = 0
for_count = 0
count = 0
avg_temp = 328

lowest = '0'
highest = '1'

z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 1  # set read timeout
#print z1serial  # debug serial.
#print z1serial.is_open  # True for opened
if z1serial.is_open:
    while True:
        size = z1serial.inWaiting()
        if size:
            data = z1serial.read(size);
            if len(data) <= 17:
                list_data = data.split(" ")
                #print list_data[0]
                #print list_data[1]
                #print list_data[2]
                sen_left = sen_left + int(list_data[0])
                sen_right = sen_right + int(list_data[1])
                sen_front = sen_front + int(list_data[2].rstrip())
                #print sen_left
                #print sen_right
                #print sen_front
                #print "Wordlwill end"
                count = count + 1 
                if count == 5:
                    avg_senLeft = sen_left/5
                    avg_senRight = sen_right/5
                    avg_senFront = sen_front/5
                    print "SenLeft  " + str(avg_senLeft)
                    print "SenRight " + str(avg_senRight)
                    print "SenDown  " + str(avg_senFront)
                    sen_left = 0
                    sen_right = 0
                    sen_front = 0
                    count = 0
                    timer = timer + 1
                    body = {'Time': timer, 'LeftExit': avg_senLeft, 'RightExit': avg_senRight, 'DownExit': avg_senFront}
                    print "Here it will send the post request"
                    #response = requests.post('http://codecademy.com/learn-http/', data=body)
                    if (avg_senLeft > avg_temp) or (avg_senRight > avg_temp) or (avg_senFront > avg_temp):
                        print "Dangor: FireAlarm initated!"
                        if (avg_senLeft > avg_senRight) and (avg_senLeft > avg_senFront):
                            print "Fire intensity is more on Left side"
                            lcd_display("Avoid left exit", 0)
                            highest = '1'
                        elif avg_senRight > avg_senFront:
                            print "Fire intenstiy is more on right side"
                            lcd_display("Avoid right exit", 0)
                            highest = '2'
                        else:
                            print "Fire intenstiy is more on front side"
                            lcd_display ("Avoid front exit", 0)
                            highest = '3'

                        if (avg_senLeft < avg_senRight) and (avg_senLeft < avg_senFront):
                            print "Fire intensity is less on Left side"
                            lcd_display ("Use left exit", 0)
                            lowest = '1'
                        elif avg_senRight < avg_senFront:
                            print "Fire intenstiy is less on right side"
                            lcd_display ("Use right exit", 0)
                            lowest = '2'
                        else:
                            print "Fire intenstiy is less on front side"
                            lcd_display("Use front exit", 0)
                            lowest = '3'
                    else:
                        lcd_display("DENSO Demo", 0)
                           
                    data=urllib2.urlopen("https://api.thingspeak.com/update?api_key=5W8LG5J0A5AHDG6W&field1="+str(avg_senLeft)+"&field2="+str(avg_senRight)+"&field3="+str(avg_senFront)+"&field4="+str(highest)+"&field5="+str(lowest))
        else:
            print 'no data'
        time.sleep(1)
else:
    print 'z1serial not open'

