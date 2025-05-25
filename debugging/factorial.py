#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrease n to avoid infinite loop
    return result

if __name__ == "__main__":
    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Error: Factorial is undefined for negative numbers")
        else:
            print(factorial(num))
    except (IndexError, ValueError):
        print("Usage: ./factorial.py <non-negative integer>")
