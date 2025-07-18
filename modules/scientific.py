import math

def evaluate_scientific_expression(expr: str):
    try:
        functions = {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "asin": lambda x: math.degrees(math.asin(x)),
            "acos": lambda x: math.degrees(math.acos(x)),
            "atan": lambda x: math.degrees(math.atan(x)),
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
            "__builtins__": {}
        }
        result = eval(expr, {"__builtins__": None}, functions)
        return result
    except Exception as e:
        return f"Error: {e}"
