import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

def main():
    st.title("Calculator App")

    num1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
    num2 = st.number_input("Enter the second number:", value=0.0, step=0.1)

    operation = st.selectbox("Select an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

    result = 0

    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    st.write("Result:", result)

if __name__ == "__main__":
    main()
