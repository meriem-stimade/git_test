from datetime import datetime


def obtenir_temps():
	return "hello ! il est {}.".format(datetime.now().strftime("%H:%M:%S"))
