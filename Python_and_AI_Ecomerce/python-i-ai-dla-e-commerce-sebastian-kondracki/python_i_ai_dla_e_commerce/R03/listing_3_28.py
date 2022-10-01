numbers = [1, 2, 4, 5, 100, 1000]

def triple(numbers):
    result = []
    for number in numbers:
        result.append(3 * number)
    return result

print(triple(numbers))