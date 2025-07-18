import math

def calculate_basic_expression(expr: str):
    try:
        safe_dict = {
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "abs": abs,
            "mod": lambda a, b: a % b,
            "pow": pow,
            "round": round,
            "floor": math.floor,
            "ceil": math.ceil,
            "pi": math.pi,
            "e": math.e,
            "__builtins__": {}
        }
        result = eval(expr, {"__builtins__": None}, safe_dict)
        return result
    except Exception as e:
        return f"Error: {e}"
