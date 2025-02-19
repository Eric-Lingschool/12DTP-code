'''little gambling game'''
import random
while True:
    try:
        b = int(input("Low range you want to bet: \n"))
        c = int(input("High range you want to bet(NO ZEROS): \n"))
        e = int(input("Money u wanna bet: \n"))
        f = int(input("Guess a number: \n"))
        d = int(c - b + 1)
        if c < b or c == 0:
            print("DO YOU NOT KNOW SIMPLE MATHEMATICS?!? DO YOU NOT UNDERSTAND WHAT LOWER AND HIGHER RANGE IS?!? OR IS IT THAT YOU CANT FOLLOW SIMPLE INSTRUCTIONS? N O  Z E R O S !\n")
            continue
        a = int(random.randint(b, c))
        g = d * e
    except ValueError:
        print("A NUMBER you degenerate.\n")
        continue
    if a == f:
        print(a)
        print(f"You win {g} dollars.\n")
    else:
        print(a)
        print("We took your money.\n")
