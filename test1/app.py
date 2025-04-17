"""Simple TODO app using Streamlit.

Run:
    pip install streamlit
    streamlit run app.py
"""
import streamlit as st

def main():
    st.title("TODO App")
    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []

    with st.form(key="add_task_form", clear_on_submit=True):
        new_task = st.text_input("New task")
        submitted = st.form_submit_button("Add")
        if submitted and new_task:
            st.session_state["tasks"].append(new_task)

    st.subheader("Tasks")
    tasks = st.session_state["tasks"]
    if not tasks:
        st.write("No tasks yet. Add a task above.")
    else:
        # Render tasks with checkboxes; collect indices of checked tasks
        to_remove = []
        for i, task in enumerate(tasks):
            if st.checkbox(task, key=f"task_{i}"):
                to_remove.append(i)
        # Remove checked tasks in reverse order to avoid index shifts
        for i in reversed(to_remove):
            key = f"task_{i}"
            if key in st.session_state:
                del st.session_state[key]
            st.session_state["tasks"].pop(i)


if __name__ == "__main__":
    main()