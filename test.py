def solve(number):
    number += 3
    number *= 2
    number -= 8
    return number


def printHello():
    print('Hello, world!')


def print3(x, y, z):
    print(x)
    print(y)
    print(z)

x = 5
x = solve(x)

y = 7
y = solve(y)

z = 11
z = solve(z)

print3(x, y, z)

printHello()