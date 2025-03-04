import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

st.title('TODO List APP with Streamlit')
st.subheader('By Qirat Saeed')

# Function to add a task
def add_task(new_task, new_status):
    st.session_state.tasks.append({'task': new_task, 'status':new_status})

# Function to edit a task
def edit_task(index, new_task, new_status):
    # if 0 <= index < len(st.session_state.tasks):  # Ensure valid index
        st.session_state.tasks[index]['task'] = new_task
        st.session_state.tasks[index]['status'] = new_status

# Function to delete a task
def delete_task(index):
    st.session_state.tasks.pop(index)

# Form for adding tasks
with st.form(key='add_task_form'):
    new_task = st.text_input('Add Task')
    new_status = st.selectbox('Status', ['Not Started', 'In Progress', 'Completed'])
    add_task_button = st.form_submit_button('Add Task')

    if add_task_button and new_task:
        add_task(new_task, new_status)
        st.success(f'Task added successfully! **{new_task}**')

# Display task list
if st.session_state.tasks:
    st.write('### Task List')
    for i, task in enumerate(st.session_state.tasks, start=1):
        st.write(f'{i}. {task["task"]} - **{task["status"]}**')

    # Task selection for editing
    task_number = st.number_input('Select task number to edit:',  min_value=1, max_value=len(st.session_state.tasks), step=1, key='task_number')

    with st.form(key='edit_task_form'):
        edit_task_input = st.text_input("Edit Task", value=st.session_state.tasks[task_number-1]['task'])
        edit_status_task = st.selectbox('Edit Status', ['Not Started', 'In Progress', 'Completed'], 
                                        index=['Not Started', 'In Progress', 'Completed'].index(st.session_state.tasks[task_number-1]['status']))
        edit_button = st.form_submit_button('Edit Task')

        if edit_button and edit_task_input:
            edit_task(task_number - 1, edit_task_input, edit_status_task)
            st.success(f'Task {task_number} updated to **{edit_task_input}** with status **{edit_status_task}**')
    
    delete_button= st.button('Delete Task')
    if delete_button:
        delete_task(task_number-1)
        st.success(f'Task *{task_number}* deleted')