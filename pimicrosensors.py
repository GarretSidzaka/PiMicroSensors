import RPi.GPIO as GPIO
import time
import os
import socket
from bottle import route, run, template, HTTPResponse
from Adafruit_BMP085 import BMP085

pirstatus=0
bmp = BMP085(0x77)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(18, GPIO.OUT)         #LED output pin
myip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
@route('/')
def getsensors():
  temp = bmp.readTemperature()
  pressure = bmp.readPressure()
  altitude = bmp.readAltitude()
  conversion = round(9.0 / 5.0 * temp + 32, 2)
  adjpressure = round(pressure / 100.0)
  i=GPIO.input(17)
  if i==0:                 #When output from motion sensor is LOW
    #print "No intruders",i
    pirstatus=0
    GPIO.output(18, 0)  #Turn OFF LED
  elif i==1:               #When output from motion sensor is HIGH
    #print "Intruder detected",i
    pirstatus=1
    GPIO.output(18, 1)  #Turn ON LED
  return template('show_sensors', conversion=conversion, adjpressure=adjpressure, altitude=altitude, pirstatus=pirstatus)


run(host=myip, port=8082, debug=True)

