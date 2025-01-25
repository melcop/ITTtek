import time
import adafruit_dht
import board

# Opsætning af sensoren - Brug GPIO4 (pin 7 på Raspberry Pi)
dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            # Læs temperatur og fugtighed fra DHT11
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            # Udskriv resultaterne
            print(f"Temperatur: {temperature}°C")
            print(f"Fugtighed: {humidity}%")

        except RuntimeError as error:
            # Ignorer midlertidige fejl (typisk for DHT-sensorer)
            print(f"Fejl ved læsning af sensor: {error.args[0]}")

        time.sleep(2.0)  # Vent 2 sekunder mellem målinger

except KeyboardInterrupt:
    print("Afslutter programmet...")

finally:
    dht_device.exit()
