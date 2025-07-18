import streamlit as st
from modules import basic_calculation, scientific, calculus, matrix
import numpy as np

st.set_page_config(page_title="Modular Scientific Calculator", layout="centered")
st.title("🧮 Modular Scientific Calculator")

if "history" not in st.session_state:
    st.session_state.history = []

mode = st.sidebar.selectbox("Choose Mode", ["Basic", "Scientific", "Calculus", "Matrix"])

# -------------- BASIC ----------------
if mode == "Basic":
    expr = st.text_input("Enter basic expression (+, -, *, /, mod)", placeholder="e.g. 10 + 5 * 3")
    if st.button("Calculate"):
        result = basic_calculation.calculate_basic_expression(expr)
        st.success(f"Result: {result}")
        st.session_state.history.insert(0, f"{expr} = {result}")

# -------------- SCIENTIFIC ----------------
elif mode == "Scientific":
    expr = st.text_input("Enter scientific expression", placeholder="e.g. sin(30) + log(100)")
    if st.button("Evaluate"):
        result = scientific.evaluate_scientific_expression(expr)
        st.success(f"Result: {result}")
        st.session_state.history.insert(0, f"{expr} = {result}")

# -------------- CALCULUS ----------------
elif mode == "Calculus":
    calc_type = st.selectbox("Operation", ["Differentiate", "Integrate", "Simplify", "Evaluate Expression"])
    expr_input = st.text_input("Enter expression (in terms of x)", placeholder="e.g. x**2 + 3*x + 2")
    if st.button("Solve"):
        try:
            if calc_type == "Differentiate":
                result = calculus.differentiate(expr_input)
            elif calc_type == "Integrate":
                result = calculus.integrate(expr_input)
            elif calc_type == "Simplify":
                result = calculus.simplify_expr(expr_input)
            elif calc_type == "Evaluate Expression":
                val = st.number_input("Enter x value:", value=1.0)
                result = calculus.evaluate_expr(expr_input, val)
            st.success(f"Result: {result}")
            st.session_state.history.insert(0, f"{calc_type}: {expr_input} → {result}")
        except Exception as e:
            st.error(f"Error: {e}")

# -------------- MATRIX ----------------
elif mode == "Matrix":
    st.write("Enter matrices (use comma-separated rows, semicolon for next row)")
    a_input = st.text_input("Matrix A", "1,2;3,4")
    b_input = st.text_input("Matrix B", "5,6;7,8")
    operation = st.selectbox("Matrix Operation", ["Add", "Subtract", "Multiply", "Determinant A", "Inverse A"])

    try:
        A = np.array([[float(num) for num in row.split(',')] for row in a_input.split(';')])
        B = np.array([[float(num) for num in row.split(',')] for row in b_input.split(';')])

        if st.button("Compute"):
            if operation == "Add":
                result = matrix.add_matrices(A, B)
            elif operation == "Subtract":
                result = matrix.subtract_matrices(A, B)
            elif operation == "Multiply":
                result = matrix.multiply_matrices(A, B)
            elif operation == "Determinant A":
                result = matrix.determinant(A)
            elif operation == "Inverse A":
                result = matrix.inverse(A)
            st.success(f"Result:\n{result}")
            st.session_state.history.insert(0, f"{operation} → {result}")
    except Exception as e:
        st.error(f"Matrix Error: {e}")

# ---------- HISTORY ----------
st.write("### 🧾 Last 10 Calculations")
for item in st.session_state.history[:10]:
    st.code(item)
