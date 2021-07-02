from sense_hat import SenseHat

sense = SenseHat()
try:
	while True:
		temperature = sense.get_temperature_from_humidity()
		humidity = sense.get_humidity()
		message = f"{temperature:.0f} C \n{humidity:.0f} %"
		sense.show_message(message)
except KeyboardInterrupt:
	sense.clear()
