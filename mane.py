def mane_function(a, b):
  if a > b:
    return a - b
  elif a < b:
    return b - a
  elif a == 0:
    return b 
  elif b == 0:
    return a

  
  def test_function(c):
    if c > 0:
      return c**2
    elif c < 0:
      return -c
    else:
      return 0
