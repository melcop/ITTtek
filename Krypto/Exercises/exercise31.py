print("""You enter a dark room with two doors.
      Do you go through door #1 , door #2 or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do y do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Talk to the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats you legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
        
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity =="2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You talk to the bear in: ")
    print("1. Danish.")
    print("2. Russian.")
    print("3. Klingon.")
    
    language = input("> ")
    
    if language == "1":
        print("Hej med dig bjørn!")
    elif language == "2":
        print("привет медведь")
    elif language == "3":
        print("chaH qo'vaD ngeD")
    else:
        print("Houston we have a problem!!")
        
else:
    print("You stumble around and fall on a knife and die. Good jon!")