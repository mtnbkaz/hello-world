import random

def get_primes():
    number = yield
    while True:
        if is_prime(number):
            number = yield number
        number += 1

def print_successive_primes(iterations, base=10):
    prime_generator = get_primes()
    print(prime_generator.send(None))
    for power in range(iterations):
        print(prime_generator.send(base ** power))