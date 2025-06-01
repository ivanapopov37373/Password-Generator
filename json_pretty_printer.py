#!/usr/bin/env python3
"""
Password Generator

Usage:
    python password_generator.py [length]

If no length is specified, default is 12.
"""

import random
import string
import sys


def generate_password(length: int = 12) -> str:
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(characters) for _ in range(length))


if __name__ == "__main__":
    try:
        length = int(sys.argv[1]) if len(sys.argv) > 1 else 12
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
