#!/usr/bin/env python

import random
import sys
from interfaces import Cypher


ALPHABET = [chr(c) for c in range(ord('a'), ord('z') + 1)]


class SubstitutionCypher(Cypher):
    def __init__(self, k: str | None) -> None:
        if k:
            self._key = list(k)
        else:
            key = list(ALPHABET)
            random.shuffle(key)
            self._key = key

    @property
    def key(self) -> object:
        return "".join(self._key)

    def encrypt(self, plaintext: str) -> str:
        return "".join([self._key[ALPHABET.index(c)] for c in plaintext])

    def decrypt(self, cyphertext: str) -> str:
        return "".join([ALPHABET[self._key.index(c)] for c in cyphertext])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        allowed_actions = {"encrypt", "decrypt"}
        action = sys.argv[1]
        if action not in allowed_actions:
            print(f"Bad argument. Allowed: {allowed_actions}, received: {action}")
            sys.exit(1)

    if len(sys.argv) > 2:
        value = sys.argv[2]

    if len(sys.argv) > 3:
        key = sys.argv[3]
    else:
        key = None

    cypher = SubstitutionCypher(key)
    value = value or input(f"value to {action}:")

    if action == "encrypt":
        print(cypher.encrypt(value))
    elif action == "decrypt":
        print(cypher.decrypt(value))
    else:
        print("Reached impossible statement.")
        sys.exit(1)

    print(f"Key used: {cypher.key}")
