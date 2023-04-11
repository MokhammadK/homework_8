def py_charm_function(x, a, b, c):
    if a == 0:
        raise ValueError("Error, 'a' cannot be 0")
    y = a*(x**2) + b*x + c
    return y

def love_or_tears(word):
    num_letters = len(word)
    if num_letters % 2 == 0:
        return "Love"