from agents.executor import ExecutorAgent

print("Testing our Game Tester System...")
print("=" * 50)

# Create executor
executor = ExecutorAgent()

# Test with sample test cases
test_cases = [
    {"id": 1, "name": "Addition Test", "description": "Testing basic addition functionality", "priority": "high"},
    {"id": 2, "name": "Division by Zero", "description": "Testing division by zero handling", "priority": "high"},
    {"id": 3, "name": "UI Layout", "description": "Testing user interface layout", "priority": "medium"}
]

print("\n Running test cases...")
for test_case in test_cases:
    result = executor.execute_test(test_case)
    print(f"Result: {result['status']} - {result['message']}")
    print("-" * 30)

executor.close()

print("\n✅ Demo completed successfully!")
print("📁 Check the 'artifacts' folder for generated test results!")