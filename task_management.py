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