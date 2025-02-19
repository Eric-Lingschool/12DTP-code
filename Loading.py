import time
list = []
print("Hi!")
ask = 0
while True:
    try:
        ask = int(input("How many seconds does it take for your patience to run out? "))
        if ask == 0:
            print("Wow, your patience in non-existant...")
            exit()
        if ask < 0:
            print("Science to this point has to find a way for time to run backwards, positive amounts please.")
        if ask > 30:
            print("Good for you, you'll become the next Elon Musk! However, I do not have that patience!")
            exit()
        break
    except ValueError:
        print("Hard to mess this up... Still, please only input whole numbers")

for i in range(0, ask):
    list.append(".")
    print("Loading ", *list, sep="", end='\r')
    time.sleep(1)
print("\n")
print("Loaded! :D")
