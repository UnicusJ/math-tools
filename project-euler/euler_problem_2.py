def problem_two():
    sum = 0
    x = 0
    y = 1
    while x < 4000000:
        if x % 2 == 0:
            sum += x
        z = (x + y)
        x = y
        y = z
    return sum
