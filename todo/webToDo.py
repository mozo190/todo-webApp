import streamlit as st

import functions

todos = functions.read_todos_txt_file()

if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""  # Initialize the session state variable


st.title('Web ToDo App')
st.subheader('A simple ToDo app to keep track of your tasks')
st.write('Welcome to the Web ToDo App!')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # If the checkbox is checked
        todos.pop(index)
        functions.write_into_todos_txt_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label='Add a new task', on_change=functions.add_todo, key='new_todo')
