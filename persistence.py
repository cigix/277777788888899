#!/usr/bin/env python3

def capabilities_with(n, mod):
    if n == 0:
        return [0]
    if mod == 1:
        return []
    res = []
    if n % mod == 0:
        if n < 10:
            res += [n]
        res += [i * 10 + mod for i in capabilities_with(n // mod, 9)]
    res += capabilities_with(n, mod -1)
    return res

def decompose(n):
    res = sorted(set(capabilities_with(n, 9)))
    if 1 < n < 10:
        res.remove(n)
    return res
