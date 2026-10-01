for zahl in range(1,31):
    if zahl % 5 == 0 and zahl % 3 == 0:
        print("FizzBuzz")
    elif zahl % 5 == 0:
        print("Buzz")
    elif zahl % 3 == 0:
        print("Fizz")
    else:
        print(zahl)

