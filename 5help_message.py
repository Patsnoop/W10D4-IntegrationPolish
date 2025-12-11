def show_help():
    """Display helpful usage examples"""
    return """


Task Manager v1.0

COMMANDS:
  add [task]       Add a new task
  list             Show all tasks
  remove [task]    Remove a task
  help             Show this message
  quit             Exit

EXAMPLES:
  > add buy milk
  > list
  > remove milk

TIP: You can use natural language! Try "create a task" or "show me all tasks"
"""

print(show_help)