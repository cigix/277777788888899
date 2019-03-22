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

if __name__ == '__main__':
    persistence = {0: 1}
    most_persistent = 0

    for i in range(1, 100):
        if i not in persistence.keys():
            persistence[i] = 1
        todo = [i]
        while todo:
            n = todo.pop(0)
            multiples = decompose(n)
            for m in multiples:
                persistence[m] = persistence[n] + 1
                if persistence[most_persistent] < persistence[m]:
                    most_persistent = m
            todo = sorted(todo + multiples)
            print(i, n, persistence[n], multiples, sep='\t')

    print("most persistent", most_persistent, "with a persistence of",
            persistence[most_persistent])
