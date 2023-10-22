import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my app!")
st.write("This app might increase your productivity or it might not:)")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="Please enter below:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
