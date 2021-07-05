from sense_hat import SenseHat
from gpiozero import CPUTemperature

FACTOR = 1

sense = SenseHat()
cpu = CPUTemperature()

try:
	while True:
		cpu_temp = cpu.temperature
		temp = sense.get_temperature_from_humidity()
		temp_calibrated = temp - ((cpu_temp - temp)/FACTOR)
		humidity = sense.get_humidity()
		message = f"{temp_calibrated:.0f} C \n{humidity:.0f} %"
		sense.show_message(message)
except KeyboardInterrupt:
	sense.clear()
