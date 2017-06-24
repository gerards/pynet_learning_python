#!/usr/bin/env python
'''

Pynet Learning Python
 - Week6 Question 1

'''

def number_sum(num1=1, num2=1, num3=1):
    " Sum the totals "
    return num1 + num2 + num3

def main():
    " main "
    print("%-3s : %-4s" % ("1a", number_sum()))
    print("%-3s : %-4s" % ("1b", number_sum(num2=2, num3=3, num1=1)))
    print("%-3s : %-4s" % ("1c", number_sum(5, num3=3, num2=2)))
    print("%-3s : %-4s" % ("1d", number_sum(5, num2=2)))

if __name__ == '__main__':
    main()
