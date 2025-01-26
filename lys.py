from gpiozero import LED, PWMLED, MotionSensor
from time import sleep

# Del 1: Teste en LED og styre dens lysstyrke med PWM
def test_led():
    led = LED(17)  # Tilslut LED til GPIO 17
    pwm_led = PWMLED(18)  # Tilslut PWM LED til GPIO 18

    print("LED blinker...")
    for _ in range(5):  # LED blinker 5 gange
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)

    print("PWM LED - styring af lysstyrke...")
    for brightness in range(0, 101, 10):  # Øg lysstyrke fra 0% til 100%
        pwm_led.value = brightness / 100.0  # Konverter procent til værdi mellem 0 og 1
        print(f"Lysstyrke: {brightness}%")
        sleep(0.2)
    pwm_led.off()  # Sluk LED

# Del 2: Teste PIR (bevægelsessensor) og styre LED
def test_pir():
    led = LED(22)  # Tilslut LED til GPIO 22
    pir = MotionSensor(23)  # Tilslut PIR sensor til GPIO 23

    print("PIR sensor er klar. Bevægelse vil tænde LED...")
    while True:
        pir.wait_for_motion()  # Vent på bevægelse
        print("Bevægelse registreret!")
        led.on()  # Tænd LED
        sleep(2)  # Hold LED tændt i 2 sekunder
        led.off()  # Sluk LED

# Hovedprogram
if __name__ == "__main__":
    try:
        print("Starter LED-test...")
        test_led()
        print("Starter PIR-test...")
        test_pir()
    except KeyboardInterrupt:
        print("\nProgram afsluttet.")