def fizzBuzz(upTo):
    for numbers in range(1, upTo):
        divisible_by_5_and_3(numbers)
        divisible_by_5(numbers)
        divisible_3(numbers)
        divisible_not_by_5_and_3(numbers)

# Using multiple functions to test different divisbilities of 5 and 3, neither, 3, or 5


def divisible_by_5_and_3(num):
    if num % 5 == 0 and num % 3 == 0:
        return print("FizzBuzz")
    else:
        pass


def divisible_by_5(num):
    if num % 5 == 0 and num % 3 != 0:
        return print("Buzz")
    else:
        pass


def divisible_3(num):
    if num % 5 != 0 and num % 3 == 0:
        return print("Fizz")
    else:
        pass


def divisible_not_by_5_and_3(num):
    if num % 5 != 0 and num % 3 != 0:
        return print(num)
    else:
        pass


fizzBuzz()
