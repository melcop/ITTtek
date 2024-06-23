import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Tid er gået!")
print("tid er gået!!")
# Brug nedtællingsuret ved at angive antal sekunder
countdown_timer(1200)  # Nedtælling fra 20 minutter