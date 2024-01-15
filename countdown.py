import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Countdown færdig!")

# Angiv antallet af sekunder for countdown
countdown_time = 420  # Ændr dette til den ønskede varighed

countdown(countdown_time)