import serial
import time

# Inicia la conexión serial en el puerto UART (ajusta el puerto y baudios según tu configuración)
ser = serial.Serial('/dev/ttyTHS1', 9600)

try:
    while True:
        ser.write("Hola desde Jetson".encode('utf-8')) # Envía un mensaje al Arduino
        time.sleep(2) # Espera un poco para la respuesta

        while ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').rstrip()
            print("Recibido: ", linea)
        time.sleep(2)
except KeyboardInterrupt:
    ser.close()
