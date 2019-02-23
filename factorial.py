def factorial(number):
    if number == 0:
        return 1
    elif number < 0:
            print("Please enter a positive number or zero None")
            # raise exception("Cannot get a factorial number")
    else:
        return number * factorial(number - 1)
        print(factorial(5))