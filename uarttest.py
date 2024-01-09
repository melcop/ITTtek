import serial
import time

COM_PORT = '/dev/serial0'  # Til Raspberry Pi Zero W
BAUD_RATE = 115200

def send_uart_data(data):
    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
        ser.write(data.encode())
        ser.close()
        print(f'Data sendt: {data}')
    except Exception as e:
        print(f'Fejl ved afsendelse af data: {str(e)}')

if __name__ == "__main__":
    # Eksempel på data, du vil sende
    data_to_send = "Hej, ESP32! Hvordan har du det?"

    send_uart_data(data_to_send)