import math
def logaritmo(n, base=10):
    if n <= 0:
        return "Error: El logaritmo solo está definido para números positivos"
    return math.log(n, base)
