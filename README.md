
# 🔬 Advanced Scientific Calculator

A fully functional, interactive, and modular **Scientific Calculator** built using Python and Streamlit. Designed to handle **basic arithmetic**, **scientific functions**, **calculus operations**, and **matrix calculations**, this calculator is ideal for students, engineers, and researchers.

---

## 📌 Features

### ✅ Basic Calculations
- Addition `+`, Subtraction `-`, Multiplication `*`, Division `/`, Modulus `%`
- Supports multi-level expressions with correct operator precedence

### ✅ Scientific Mode
- Trigonometric functions: `sin`, `cos`, `tan` (degrees)
- Logarithmic & exponential functions: `log`, `ln`, `e`, `pi`
- Square root and absolute value
- Angle conversions and complex math operations

### ✅ Calculus Mode
- Symbolic **Differentiation**
- Symbolic **Integration**
- Expression Simplification
- Evaluate expressions at specific `x` values using **SymPy**

### ✅ Matrix Mode
- Matrix addition, subtraction, multiplication
- Determinants, transpose, and inverse
- 2D, 3D, and even 4D matrix operations using **NumPy**

### ✅ History Tracking
- Stores the **last 10 calculations**
- Easily view past computations across all modes

---
## 🧱 Project Structure

```plaintext
scientific_calculator/
│
├── app.py                      # Main Streamlit interface
├── requirements.txt
│
├── modules/
│   ├── basic_calculation.py    # For +, -, *, /, modulus
│   ├── scientific.py           # sin, cos, tan, log, ln, etc.
│   ├── calculus.py             # diff, integration, simplify, etc.
│   └── matrix.py               # 2D/3D/4D matrix operations
