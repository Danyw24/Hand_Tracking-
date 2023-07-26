import serial

# Configuración del puerto serie
port = "/dev/ttyACM0"  # Reemplaza con el puerto correcto en tu sistema
baudrate = 9600

# Inicializar la conexión del puerto serie
arduino = serial.Serial(port, baudrate)

# Enviar el número 1
data = b'1'  # El número 1 como bytes
arduino.write(data)

# Cerrar la conexión del puerto serie
arduino.close()