import adafruit_bme680
import time
import board
i2c=board.I2C()
bme680=adafruit_bme680.Adafruit_BME680_I2C(i2c)
bme680.seal_level_pressure=1013.25
t=1
zeff=[]
while t<10:
	
	print("time:")
	print(t)
	print("\nTemperature: %0.1f C" %bme680.temperature)
	print("Gas: %d ohm" %bme680.gas)
	print("humidity:%0.1f %%" %bme680.relative_humidity)
	print("Pressure: %0.3f hpa" %bme680.pressure)
	print("Altitude = %0.2f meters" %bme680.altitude)
	
	jeff= [t,bme680.temperature, bme680.gas,bme680.relative_humidity,bme680.pressure,bme680.altitude]
	print(jeff)
	t=t+1
	
	zeff.append(jeff)
	time.sleep(2)
	
print(zeff)
