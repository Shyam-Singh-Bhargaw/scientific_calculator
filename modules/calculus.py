import sympy as sp

x = sp.symbols('x')

def differentiate(expr_input: str):
    expr = sp.sympify(expr_input)
    return sp.diff(expr, x)

def integrate(expr_input: str):
    expr = sp.sympify(expr_input)
    return sp.integrate(expr, x)

def simplify_expr(expr_input: str):
    expr = sp.sympify(expr_input)
    return sp.simplify(expr)

def evaluate_expr(expr_input: str, value: float):
    expr = sp.sympify(expr_input)
    return expr.subs(x, value).evalf()
