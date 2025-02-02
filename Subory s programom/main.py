import utime
import BME280
from machine import Pin, SoftI2C, ADC
import machine

i2c = SoftI2C(scl=Pin(6), sda=Pin(5), freq=400000)

soil = machine.ADC(machine.Pin(1))

relay1 = Pin(8, Pin.OUT)
relay2 = Pin(7, Pin.OUT)

min_moisture=0
max_moisture=65535

while True:
 
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure
  moist = (100-(max_moisture-soil.read_u16())*100/(max_moisture-min_moisture))
  
  
  relay1.value(1)
  relay2.value(0)
  utime.sleep(1)

  print('Teplota: ', temp)

  print('Relatívna vlhkosť vzduchu: ', hum)
     
  print('Tlak: ', pres)
  
  print("Vlhkosť pôdy:" + "%.2f" % moist +"% (adc: "+str(soil.read_u16())+")")
  
  utime.sleep(0.5)
  
  relay1.value(0)
  relay2.value(1)
  utime.sleep(1)

  utime.sleep(1)
  #machine.lightsleep(6000)
