from datetime import datetime as dt
from js import console

tasks = []

# define the task template that will be use to render new templates to the page
task_template = Element("task-template").select('.task', from_content=True)
task_list = Element("list-tasks-container")
new_task_content = Element("new-task-content")

def add_task(*ags, **kws):
  # create task
  task_id = f"task-{len(tasks)}"
  task = {"id": task_id, "content": new_task_content.element.value, "done": False, "created_at": dt.now()}
  tasks.append(task)
  
  # add the task element to the page as new node in the list by cloning from a template
  taskHtml = task_template.clone(task_id, to=task_list)
  taskHtmlContent = taskHtml.select('p')
  taskHtmlContent.element.innerText = task['content']
  taskHtmlCheck = taskHtml.select('input')
  task_list.element.appendChild(taskHtml.element)
  
  def check_task(evt=None):
    task['done'] = not task['done']
    if task['done']:
      taskHtmlContent.element.classList.add("line-through")
    else:
      taskHtmlContent.element.classList.remove("line-through")

  new_task_content.clear()
  taskHtmlCheck.element.onclick = check_task

def add_task_event(e):
  console.log("im in")
  if (e.key == "Enter"):
    add_task()