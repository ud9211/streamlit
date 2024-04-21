import streamlit as st

st.title('Find the Largest Number among three numbers')

num1 = st.number_input('Enter first number', value=0)
num2 = st.number_input('Enter second number', value=0)
num3 = st.number_input('Enter third number', value=0)

def find_largest(x, y, z):
    return max(x, y, z)

if st.button('Find Largest'):
    result = find_largest(num1, num2, num3)
    st.success(f'The largest number is {result}')
