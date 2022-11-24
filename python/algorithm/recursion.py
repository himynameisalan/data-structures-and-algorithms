def factorialRecursive(number: int):
    if number < 1:
        return 0
    if number == 1:
        return 1

    return number * factorialRecursive(number - 1)


def factorialIterative(number: int):
    if number < 1:
        return 0
    if number == 1:
        return 1

    result = 1

    for i in range(number, 1, -1):
        result = result * i

    return result


# print(factorialRecursive(5))
# print(factorialIterative(5))

def fibonacciRecursive(index: int):
    if index <= 1:
        return index

    return fibonacciRecursive(index - 1) + fibonacciRecursive(index - 2)


def fibonacciIterative(index: int):
    if index <= 1:
        return index

    array = []

    for i in range(0, index):
        if i <= 1:
            array.append(i)
        else:
            array.append(array[i - 1] + array[i - 2])

    return array[index - 1] + array[index - 2]


# print(fibonacciRecursive(0))
# print(fibonacciRecursive(1))
# print(fibonacciRecursive(2))
# print(fibonacciRecursive(8))
# print(fibonacciIterative(0))
# print(fibonacciIterative(1))
# print(fibonacciIterative(2))
# print(fibonacciIterative(7))


# Implement a function that reverses a string using iteration...and then recursion!
def reverseString(text: str):
    if len(text) < 1:
        return ''

    return reverseString(text[1:]) + text[0]


# should return: 'yretsam oyoy'
print(reverseString('yoyo mastery'))
