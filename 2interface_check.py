# WRONG: Component A returns string, Component B expects list

# component_a.py
def get_tasks():
    return "task1,task2,task3"  # Returns string

# component_b.py
def count_tasks(tasks):
    return len(tasks)  # Expects list, will count characters!

# Result: count_tasks gets "task1,task2,task3" and returns 17 (characters)
# instead of 3 (tasks)




# Solution: Verify interface contacts:

# integration_test.py
def test_get_tasks_returns_list():
    """Verify get_tasks returns list, not string"""
    from src.storage import get_tasks
    
    result = get_tasks()
    assert isinstance(result, list), f"Expected list, got {type(result)}"
    print("✓ get_tasks returns correct type")


def test_count_tasks_accepts_list():
    """Verify count_tasks works with list input"""
    from src.utils import count_tasks
    
    test_list = ["task1", "task2"]
    result = count_tasks(test_list)
    assert result == 2
    print("✓ count_tasks works with list")

