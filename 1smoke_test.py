# smoke_test.py
"""
Minimal test to see if system imports and runs.
"""
import src

def test_system_imports():
    """Can we import all components?"""
    try:
        from src import cli, intents, storage
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False


def test_basic_run():
    """Can we call the main function?"""
    try:
        from src.cli import run_cli
        # Don't actually run the loop, just import
        print("✓ CLI function accessible")
        return True
    except Exception as e:
        print(f"✗ CLI import failed: {e}")
        return False


if __name__ == "__main__":
    print("=== SMOKE TEST ===")
    imports_ok = test_system_imports()
    cli_ok = test_basic_run()
    
    if imports_ok and cli_ok:
        print("\n✓ SMOKE TEST PASSED")
    else:
        print("\n✗ SMOKE TEST FAILED")