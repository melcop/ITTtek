from gpiozero import LED, MotionSensor
from time import sleep

# Opsætning af GPIO-pins
led = LED(17)  # LED tilsluttet pin GPIO 17
pir = MotionSensor(4)  # PIR sensor tilsluttet pin GPIO 4

def blink_led():
    """Får LED til at blinke."""
    print("Starter LED-blink...")
    for _ in range(10):  # Blink 10 gange
        led.on()
        sleep(0.5)  # LED tændt i 0,5 sekunder
        led.off()
        sleep(0.5)  # LED slukket i 0,5 sekunder
    print("LED-blink afsluttet.")

def motion_detected():
    """Registrerer bevægelse og tænder LED."""
    print("Bevægelse registreret! LED tændt.")
    led.on()
    sleep(2)  # Hold LED tændt i 2 sekunder
    led.off()
    print("LED slukket.")

def main():
    """Hovedprogram."""
    try:
        # Test LED-blink
        blink_led()

        # Registrer bevægelse
        print("PIR-sensor aktiveret. Vent på bevægelse...")
        while True:
            pir.wait_for_motion()  # Vent til bevægelse registreres
            motion_detected()
            pir.wait_for_no_motion()  # Vent til der ikke længere er bevægelse
    except KeyboardInterrupt:
        print("\nAfslutter programmet.")
    finally:
        led.off()  # Sørg for at LED er slukket, når programmet afsluttes

if __name__ == "__main__":
    main()