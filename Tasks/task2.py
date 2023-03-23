def f(a, b):
    if b < 0 < a:
        a, b = b, a
    if b == 0:
        return a
    return f(a + 1, b - 1)

n = int(input())
m = int(input())
print(f(n, m))