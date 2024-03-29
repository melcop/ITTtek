import time
import winsound

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Countdown færdig!")
    # Afspil en lyd ved afslutningen af countdown
    winsound.Beep(700, 12000)  # Juster frekvens (1000 Hz) og varighed (1000 ms) efter behov

# Angiv antallet af sekunder for countdown
countdown_time = 420  # Ændr dette til den ønskede varighed
print("tid er sat til 7 minutter og bip lyd er sat til 12 sekonder")
countdown(countdown_time)