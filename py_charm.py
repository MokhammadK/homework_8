def py_charm_function(x, a, b, c):
    if not isinstance(x, (int, float)) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Error, all inputs must be numeric")
    if a == 0:
        raise ValueError("Error, 'a' cannot be 0")
    y = a*(x**2) + b*x + c
    return y

