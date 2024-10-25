import streamlit as st

import functions

todos = functions.read_todos_txt_file()

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""  # Initialize the session state variable

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_into_todos_txt_file(todos)
    st.session_state["new_todo"] = "" # Reset the input field


st.title('Web ToDo App')
st.subheader('A simple ToDo app to keep track of your tasks')
st.write('Welcome to the Web ToDo App!')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Add a new task', on_change=add_todo, key='new_todo')
