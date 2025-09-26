from agents.planner import PlannerAgent
from agents.ranker import RankerAgent

print("🔍 Verifying the fix...")

# Test Planner
planner = PlannerAgent()
test_cases = planner.generate_test_cases()
print(f"✅ Planner generated {len(test_cases)} test cases")

# Test Ranker
ranker = RankerAgent()
top_tests = ranker.rank_tests(test_cases)
print(f"✅ Ranker selected top {len(top_tests)} tests")

print("🎉 System is working! Now run: python -m uvicorn main:app --reload")