def py_charm_function(x, a, b, c):
    if not isinstance(x, (int, float)) or not isinstance(a, (int, float)) or not isinstance(b, (
    int, float)) or not isinstance(c, (int, float)):
    if a == 0:
        raise ValueError("Error, 'a' cannot be 0")
    y = a*(x**2) + b*x + c
    return y

def love_or_tears(word):
    num_letters = len(word)
    if num_letters % 2 == 0:
        return "Love"
    else:
        return "Tears"