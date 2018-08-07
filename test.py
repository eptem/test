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

x = solve(5)

y = solve(7)

z = solve(11)

print3(x, y, z)

printHello()