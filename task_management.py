class Task:
  def __init__(self, task_id, description, assigned_to=None, completed=False):
    self.task_id = task_id
    self.description = description
    self.assigned_to = assigned_to
    self.completed = completed

  def assign_task(self, user):
    self.assigned_to = user

  def mark_completed(self):
    self.completed = True


class User:
  def __init__(self, user_id, name):
    self.user_id = user_id
    self.name = name

class TaskManager:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def list_tasks(self, status=None):
    if self.tasks is None:
      return self.tasks
    return [tasks for tasks in self.tasks if tasks.complete == status]