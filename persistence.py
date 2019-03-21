#!/usr/bin/env python3

def decompose(n):
    def decompose_inner(n):
        print("decompose({})".format(n))
        if n == 0:
            return [0]
        def decompose_step(n, mod):
            print("    step({}, {})".format(n, mod))
            if mod == 1:
                return []
            if n % mod == 0:
                return [mod] + decompose_inner(n // mod)
            return decompose_step(n, mod - 1)
        return decompose_step(n, 9)
    return sorted(decompose_inner(n))

print(decompose(54))
