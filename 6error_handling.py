def handle_intent(intent: str, slots: dict) -> str:
    if intent == "DELETE":
        task_name = slots.get("task", "").strip()
        
        if not task_name:
            # [What happened] + [What to do]
            return "I didn't catch which task to remove. Try: remove [task name]"
        
        success = remove_task(task_name)
        
        if success:
            # Positive confirmation
            return f"✓ Removed '{task_name}'"
        else:
            # [What happened] + [Why] + [What to do]
            return f"Task '{task_name}' not found. Type 'list' to see all tasks."
