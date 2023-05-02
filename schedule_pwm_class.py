import schedule
import time
from gpiozero import OutputDevice
import pigpio

# Global variables
RED_LED_GPIO_PIN = 13
BLUE_LED_GPIO_PIN = 26

class LightScheduler(object):
    """A Python class to turn on/off lights"""
    def __init__(self, LED_GPIO):
        self.LED_GPIO = LED_GPIO
        self.pi = pi = pigpio.pi()
        self.pi.set_PWM_range(LED_GPIO, 100)
        self.timeList = []
        self.dutyList = []
    
    def add_schedule(self, time, duty):
        self.timeList.append(time)
        print(self.timeList)
        self.dutyList.append(duty)
        print(self.dutyList)
    
    def init_schedule(self):
        # set the schedule
        for i in range(len(self.dutyList)):
            print(i)
            # .do second parameter is parameter given to the set_duty function
            schedule.every().day.at(self.timeList[i]).do(self.set_duty, self.dutyList[i])

    def set_duty(self, duty):
        """Sets dutycycle for LED"""
        print(f"Setting duty to : {duty}")
        self.pi.set_PWM_dutycycle(self.LED_GPIO, duty)

if __name__ == "__main__":
    red = LightScheduler(RED_LED_GPIO_PIN)
    red.add_schedule("18:42", 60)
    red.add_schedule("18:43", 0)
    red.init_schedule()

    blue = LightScheduler(BLUE_LED_GPIO_PIN)
    blue.add_schedule("18:42", 60)
    blue.add_schedule("18:43", 0)
    blue.init_schedule()
    while True:
        schedule.run_pending()
        time.sleep(1)