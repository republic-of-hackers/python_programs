#!/bin/python3

import sys

def leftRotation(a, d):
    for _ in range(d):
        t = a[0]
        a.remove(a[0])
        a.append(t)
    return a

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))


