number = int(input("Please enter a number: "))

def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 != 0):
        print("Fizz")
    elif (x % 5 == 0) and (x % 3 != 0):
        print("Buzz")
    elif (x % 3 == 0) and (x % 5 == 0):
        print ("Fizz Buzz")
    else:
        print ("Number is not divisible by 3 or 5.")

fizzbuzz(number)
