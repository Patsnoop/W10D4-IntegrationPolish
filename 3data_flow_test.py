# integration_test.py
def test_full_add_task_flow():
    """
    Test complete flow: CLI input → Intent detection → Storage → Response
    """
    from src.intents import detect_intent, handle_intent
    from src.storage import load_tasks, clear_tasks
    
    # Setup: clear any existing tasks
    clear_tasks()
    
    # Simulate user input
    user_input = "add buy milk"
    
    # Step 1: Detect intent
    intent, slots = detect_intent(user_input)
    assert intent == "CREATE", f"Expected CREATE, got {intent}"
    assert slots.get("task") == "buy milk", f"Task not extracted correctly"
    
    # Step 2: Handle intent (should add to storage)
    response = handle_intent(intent, slots)
    assert "Added" in response or "✓" in response
    
    # Step 3: Verify storage updated
    tasks = load_tasks()
    assert "buy milk" in tasks, "Task not saved to storage"
    
    print("✓ Full add task flow works end-to-end")


# Callouts to Say
# "This tests the data path through all layers: CLI → Logic → Data"
# "If this passes, you know components are connected correctly"
