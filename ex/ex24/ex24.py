#! /usr/bin/python3

def factorial_recursive(num):
    if num == 1:
        return 1
    else:
        return factorial_recursive(num - 1) * num


def factorial_loop(num):
    value = 1
    count = 1
    while count < num:
        count += 1
        value *= count
    return value


def fibonacci_recursive(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)


def fibonacci_loop(number):
    if number == 1:
        return 1
    else:
        first = 0
        second = 1
        count = 1
        while count < number:
            count += 1
            value = first + second
            first = second
            second = value
        return value


def count_down_recursive(num):
    print(num, end=' ')
    if num > 1:
        count_down_recursive(num - 1)


def count_down_loop(num):
    for n in range(num, 0, -1):
        print(n, end=' ')


print('factorial_recursive(10):', factorial_recursive(10))
print('factorial_loop(10):', factorial_loop(10))
print()
print('The first 10 Fibonacci numbers using recursion')
for n in range(1, 11):
    print(fibonacci_recursive(n), end=' ')
print()
print('The first 10 Fibonacci numbers using a loop')
for n in range(1, 11):
    print(fibonacci_loop(n), end=' ')
print()
print()
print('count_down_recursive(10)')
count_down_recursive(10)
print()
print('count_down_loop(10)')
count_down_loop(10)
