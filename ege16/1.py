f = lambda x: 1 if x == 1 else 2 * f(x - 1) + x + 1

print(f(19))
