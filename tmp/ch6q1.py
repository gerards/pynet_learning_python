#!/usr/bin/env python
'''

ch6q1

Create a function that returns the multiplication product of three parameters--x, y, and z. z should have a default value of 1.
    a. Call the function with all positional arguments.
    b. Call the function with all named arguments.
    c. Call the function with a mix of positional and named arguments.
    d. Call the function with only two arguments and use the default value for z.

'''

def multiply(num1, num2, num3=1):
    ' multiplyyyyy '

    return num1 * num2 * num3


def main():
    ' MAIN! '
    number1 = 1
    number2 = 5
    number3 = 2

    '''
    a. positional args:
    output = multiply(number1, number2, number3)

    b. named args:
    output = multiply(num1=number1, num2=number2, num3=number3)

    c. mix of postitional and named args:
    output = multiply(number1, num3=number3, num2=number2)

    d. two args and default for z:
    output = multiply(number1, num2=number2)
    '''

    output = multiply(number1, num2=number2)
    print("%s * %s * %s = %s" % (number1, number2, number3, output))


if __name__ == '__main__':
    main()
