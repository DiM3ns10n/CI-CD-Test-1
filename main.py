import streamlit as st
from basic_calculator import BasicCalculator

st.title("Basic Calculator")
st_input = st.text_input("Enter numbers separated by commas")
st_radio = st.radio("Select operation", ["Add", "Subtract", "Multiply", "Divide"], key = "operation", index = None)

if "calculation_result" not in st.session_state:
    st.session_state["calculation_result"] = None

def check_digits(st_input):
    digits = st_input.split(",")
    is_digit = all(item.isdigit() for item in digits)
    return is_digit

def calculate(st_input, st_radio):
    is_digit = check_digits(st_input)
    if not is_digit:
        st.error("Please enter only digits")
        return
    else:
        arguments = tuple(map(int, st_input.split(",")))
        calculator = BasicCalculator(arguments)
        if st_radio == "Add":
            result = calculator.add()
        elif st_radio == "Subtract":
            result = calculator.subtract()
            
        elif st_radio == "Multiply":
            result = calculator.multiply()
            
        elif st_radio == "Divide":
            result = calculator.divide()
          
        st.session_state["calculation_result"] = result

st_calculate_result = st.button("Calculate", key="calculate", on_click= calculate, args=(st_input, st_radio))

if st_calculate_result and st.session_state["calculation_result"] is not None:
    st.write(f"Result of {st_radio}: {st.session_state['calculation_result']}")



