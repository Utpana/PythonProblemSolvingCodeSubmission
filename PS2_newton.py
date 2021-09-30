
# Problem Set 2
# Name: Utpana
# Time Spent: 5:00hrs

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.
    Example:
    poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    x = -13
    print(evaluate_poly(poly, x))  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9
    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    value = 0
    for i in range(0,len(poly)):
        value = value + poly[i]*(x**i)
    return value

def compute_deriv(poly):
    tup = ()
    for i in range(1,len(poly)):
        derv = poly[i]*i
        tup = tup + (derv,)
    return tup

def compute_root(poly,x_0,epsilon):
    iteration = 0
    x = x_0
    f_x = evaluate_poly(poly,x)
    derv_f_x =  evaluate_poly(compute_deriv(poly), x)
    while abs(f_x) >= epsilon:
        iteration += 1
        f_x = evaluate_poly(poly,x)
        derv_f_x =  evaluate_poly(compute_deriv(poly), x)
        x = x - (f_x/derv_f_x)
    return (x, iteration)    

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = 0.0001
print(compute_root(poly, x_0, epsilon))
