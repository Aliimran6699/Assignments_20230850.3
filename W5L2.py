import random


def generate_unique_random_numbers(n):
    if n > 20:
        print("Error: n cannot be greater than 20.")
        return []

    numbers = set()
    while len(numbers) < n:
        numbers.add(random.randint(1, 20))

    return list(numbers)


# Example usage:
random_numbers = generate_unique_random_numbers(10)
print(random_numbers)
