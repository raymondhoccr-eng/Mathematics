#!/usr/bin/env python3

import math
import sys
from typing import List, Tuple


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3

    limit: int = int(math.isqrt(n))
    factor: int = 5
    while factor <= limit:
        if n % factor == 0 or n % (factor + 2) == 0:
            return False
        factor += 6
    return True


def normalize_range(a: int, b: int) -> Tuple[int, int]:
    """Return an ordered (start, end) tuple where start <= end."""
    return (a, b) if a <= b else (b, a)


def primes_in_range(start: int, end: int) -> List[int]:
    start, end = normalize_range(start, end)
    start = max(start, 2)
    return [value for value in range(start, end + 1) if is_prime(value)]


def main() -> None:
    # Prefer CLI args for non-interactive use: python prime_range.py 10 50
    if len(sys.argv) >= 3:
        try:
            start_value = int(sys.argv[1])
            end_value = int(sys.argv[2])
        except ValueError:
            print("Error: start and end must be integers.")
            sys.exit(1)
    else:
        # Fallback to interactive prompts if args are not provided
        try:
            start_value = int(input("Enter start of range: "))
            end_value = int(input("Enter end of range: "))
        except ValueError:
            print("Error: start and end must be integers.")
            sys.exit(1)

    prime_numbers = primes_in_range(start_value, end_value)
    if prime_numbers:
        print(" ".join(map(str, prime_numbers)))
    else:
        print("No primes in the given range.")


if __name__ == "__main__":
    main()