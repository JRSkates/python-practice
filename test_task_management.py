from task_management import Task, User, TaskManager

def test_task_management():
  user1 = User(1, "Alice")
  user2 = User(2, "Bob")

  task1 = Task(1, "Complete project tasks")
  task2 = Task(2, "Review documentation")
  task3 = Task(3, "Prepare presentation", assigned_to=user1, completed=True)

  task_manager = TaskManager()
  task_manager.add_task(task1)
  task_manager.add_task(task2)
  task_manager.add_task(task3)

  # Test adding taska and listing all tasks
  assert len(task_manager.list_tasks()) == 3

  # Test listing incomplete tasks
  assert len(task_manager.list_tasks(status=False)) == 2

  # Test listing completed tasks
  assert len(task_manager.list_tasks(status=True)) == 1

  # Test assigning a task and marking it as completed
  assert task1.assigned_to is None
  task1.assign_task(user1)
  assert task1.assigned_to == user1
  assert not task1.completed
  task1.mark_completed()
  assert task1.completed