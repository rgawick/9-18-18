number = int(input("Please enter a number to see if it is even or odd: "))

def even_or_odd(x):
    if(x % 2 == 0):
        print("Even")
    else:
        print("Odd")

even_or_odd(number)
