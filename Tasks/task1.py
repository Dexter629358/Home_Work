def pow(a, b):
    if b == 0:
        return 1
    if b < 0:
        return pow(a, b + 1) * 1 / a
    return pow(a, b - 1) * a

print(pow(int(input()), int(input())))