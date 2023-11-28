import Jetson.GPIO as GPIO
import time

# Configura el modo del pin (BOARD o BCM)
GPIO.setmode(GPIO.BOARD) # o GPIO.setmode(GPIO.BCM)

# Configura el pin como entrada
pinEntrada = 12  # Cambia esto por el número de tu pin
GPIO.setup(pinEntrada, GPIO.IN)

try:
    while True:
        estado_pin = GPIO.input(pinEntrada)
        print("Estado del Pin: ", estado_pin)
        time.sleep(0.5)  # Medio segundo de espera
except KeyboardInterrupt:
    GPIO.cleanup()

