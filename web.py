import streamlit as st
import functions

todos = functions.get_todos()
print(todos)

st.title("My Todo App")
st.subheader("this is my todo app")

st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(key = label='', placeholder='Life of Brian')

