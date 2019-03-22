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
    persistence = dict()
    for i in range(10):
        persistence[i] = 1
    todo = list(range(1, 10))
    most_persistent = 0
    while todo:
        n = todo.pop(0)
        multiples = decompose(n)
        for m in multiples:
            persistence[m] = persistence[n] + 1
            if persistence[most_persistent] < persistence[m]:
                most_persistent = m
            print("persistence of", m, "is", persistence[m])
        todo = sorted(todo + multiples)
        print(n, persistence[n], multiples, sep='\t')
    print("most persistent", most_persistent, "with a persistence of",
            persistence[most_persistent])
