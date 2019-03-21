#!/usr/bin/env python3

NaN = float('NaN')

def decompose_mod(n, mod):
    #print("   decompose_mod({}, {})".format(n, mod))
    if mod == 1:
        return NaN
    if n % mod == 0:
        return decompose_factor(n // mod) * 10 + mod
    return decompose_mod(n, mod - 1)

def decompose_factor(n):
    #print("decompose_factor({})".format(n))
    if n == 1:
        return 0
    return decompose_mod(n, 9)

def decompose(n):
    if n < 10:
        return 10 + n
    return decompose_factor(n)
