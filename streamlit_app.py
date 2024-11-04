import streamlit as st

#write a statement
st.write("Hello World")

#using button
st.header('st.button')
if st.button('say hello'):
    st.write('Why hello')
else:
    st.write('Goodbye')