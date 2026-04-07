# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
   discriminant = b**2 - 4*a*c
   if discriminant > 0:
    r1 = (-b + pow(discriminant, 0.5)) / (2*a)
    r2 = (-b - pow(discriminant, 0.5)) / (2*a)
    return f"({r1}, {r2})"
   elif discriminant == 0:
        r = -b / (2*a)
        return f"({r})"
   else:
        return "( )"
   
def value_y(a, b, c, x):
    return (a * x**2 + b * x + c)


def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    
def derivation(a, b, c):
    if a == 0 and b == 0:
        return f"f'(x) = 0"
    elif a==0 and b!=0:
        return f"f'(x) = {b}"
    elif a!=0 and b==0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {2*a} * X + {b}"

print(roots(1, -3, 2))
print(value_y(1, -3, 2, 0))  
print(to_string(2, -3, 1)) 
print(derivation(2, -3, 1))

