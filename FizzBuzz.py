for numero in range (1,31):
    if numero % 3 == 0 and numero % 5 == 0:
        print("fizzBuzz")
    elif numero % 3 == 0:
        print("fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)