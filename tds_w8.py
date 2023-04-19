import streamlit as st

# Suppress a warning that may appear when using certain plotting libraries in Colab
st.set_option('deprecation.showPyplotGlobalUse', False)

def largest_num(num1, num2, num3):
    """
    Function to find the largest among three given numbers
    """
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

st.sidebar.title("Find the largest number")
st.sidebar.write("Enter three numbers below:")

num1 = st.sidebar.number_input("Enter the first number:")
num2 = st.sidebar.number_input("Enter the second number:")
num3 = st.sidebar.number_input("Enter the third number:")

if st.sidebar.button("Find the largest number"):
    largest = largest_num(num1, num2, num3)
    st.success("The largest number is {}".format(largest))
