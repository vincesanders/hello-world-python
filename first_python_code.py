print("Hello World!")
### floor division
print(9//4)
### exponents
print(3**3)
print(type(3.2))
x = 'x'
x = 1
print(x)
### using + and * with strings
first = 'ice'
second = 'cream'
print(first + second)
print(first * 2 + 'baby') # too cold, too cold
'''
Here is a
multiline string
that I am using as a comment
'''
"""
You can also use
double quotes
"""
### My first python function
def add_numbers(num1, num2):
    print(num1 + num2)
add_numbers(2, 3)
### for loops
for i in range(4):
    print('loop ' + str(i))
### if else statements
if x < 0:
    print('x is less than 0')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is 0')
def right_justify(string):
    return ((70 - len(string)) * ' ') + string
print(right_justify(first))
### Challenges
### Exercise 1
def secondsInMinutes(m):
    return 60 * m
def kilometersToMiles(k):
    return k * 0.621371
def printSecondsToMinutes(s):
    minutes = s // 60
    solution = str(minutes) + ' minutes'
    if s % 60 != 0:
        seconds = s % 60
        solution += ' and ' + str(seconds) + ' seconds'
    return solution
def timeInSecondsPerMile(k, min, sec):
    return (secondsInMinutes(min) + sec) / kilometersToMiles(k)
def averageSpeedMPH(k, min, sec):
    t = secondsInMinutes(min) + sec
    multiplier = 3600 / t
    return kilometersToMiles(k) * multiplier
print('How many seconds are there in 21 minutes and 15 seconds? ' + str(secondsInMinutes(21) + 15))
print('How many miles are there in 5 kilometers? ' + str(kilometersToMiles(5)) + ' miles')
print('If you run a 5 kilometer race in 21 minutes and 15 seconds, what is your average pace (time per mile in minutes and seconds)?')
print(printSecondsToMinutes(timeInSecondsPerMile(5, 21, 15)) + ' per mile')
print('What is your average speed in miles per hour? ' + str(averageSpeedMPH(5, 21, 15)) + ' mph')
def totalWholesaleCost(totalBought):
    return 19.95 * 0.25 * totalBought + 2.5 + totalBought - 1
print('Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. Shipping costs $2.50 for the first copy and $1 for each additional copy. What is the total wholesale cost for 75 copies?')
print('The total cost is $' + str(totalWholesaleCost(75)) + '.')
### Exercise 2
def do_twice(f, v):
    f(v)
    f(v)
do_twice(print, 'spam')
def print_twice(v):
    print(v)
    print(v)
do_twice(print_twice, 'spam')
def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)
do_four(print, 'more spam')
### Exercise 3
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')
a = int(input('Enter an integer: '))
b = int(input('Enter an integer: '))
c = int(input('Enter an integer: '))
n = int(input('Enter an integer: '))
check_fermat(a, b, c, n)