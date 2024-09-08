#!/usr/bin/python3
""" Prime Game
"""


def count_primes_up_to(n):
    """ Function to count prime numbers up to n using the Sieve of
    Eratosthenes. """
    if n < 2:
        return 0

    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    return sum(prime)


def isWinner(x, nums):
    """ Function to determine the winner based on the number of rounds """
    if x == 0 or any(num <= 0 for num in nums):
        return None  # Return None for 0 rounds or invalid numbers

    Ben = 0
    Maria = 0

    for num in nums:
        if num == 1:
            Ben += 1
        else:
            count = count_primes_up_to(num)
            if count % 2 == 1:
                Maria += 1
            else:
                Ben += 1

    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    else:
        return None
