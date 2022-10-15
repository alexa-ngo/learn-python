def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d

t = ['apple', 'banana', 'grapes', 'mango', 'apple', 'mango',]
print(histogram(t))
