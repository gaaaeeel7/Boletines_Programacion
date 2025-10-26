print("Fahrenheit    Celsius")
for f in range(0, 121, 10):
    c = (f - 32) * 5 / 9
    print(f"{f}, {c}")