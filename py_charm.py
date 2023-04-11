def py_charm_function(x, a, b, c):
    if a == 0:
        raise ValueError("Error, 'a' cannot be 0")
    y = a*(x**2) + b*x + c
    return y