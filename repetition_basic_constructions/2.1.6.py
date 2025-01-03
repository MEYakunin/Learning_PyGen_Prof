def same_parity(numbers):
    numbers = list(filter(lambda num: num % 2 == numbers[0] % 2, numbers))
    return numbers


print(same_parity([6, 0, 67, -7, 10, -20]))