def test_invalid_input_handling():
    """Test that bad inputs don't crash the system"""
    from src.intents import detect_intent, handle_intent
    
    # Test empty input
    intent, slots = detect_intent("")
    response = handle_intent(intent, slots)
    assert "help" in response.lower() or "try" in response.lower()
    
    # Test gibberish
    intent, slots = detect_intent("asdfghjkl")
    response = handle_intent(intent, slots)
    assert response is not None and len(response) > 0
    
    # Test missing slot
    intent, slots = detect_intent("add")  # No task name
    response = handle_intent(intent, slots)
    assert "specify" in response.lower() or "name" in response.lower()
    
    print("✓ Error paths handled gracefully")
