import streamlit as st
import functions
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)


todos = functions.get_todos()


st.title("My Todo App")
st.subheader("this is my todo app")

st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo , key = "test")

st.text_input(label='', placeholder='Life of Brian',
              on_change=add_todo, key='new_todo')
print(st.session_state)