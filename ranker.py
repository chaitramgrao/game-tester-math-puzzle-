class RankerAgent:
    def __init__(self):
        self.priority_weights = {"high": 3, "medium": 2, "low": 1}
        self.category_weights = {"functional": 2.5, "error": 3, "performance": 2, "usability": 1.5, "compatibility": 1}
    
    def rank_tests(self, test_cases):
        print(" RankerAgent ranking test cases...")
        
        scored_tests = []
        for test in test_cases:
            score = self.calculate_test_score(test)
            scored_tests.append((test, score))
        
        # Sort by score descending
        scored_tests.sort(key=lambda x: x[1], reverse=True)
        
        # Select top 10
        top_tests = [test for test, score in scored_tests[:10]]
        
        print(f" Selected top 10 tests from {len(test_cases)} candidates")
        for i, (test, score) in enumerate(scored_tests[:10], 1):
            print(f"   {i}. {test['name']} (Score: {score:.2f}, Priority: {test['priority']})")
        
        return top_tests
    
    def calculate_test_score(self, test_case):
        priority_score = self.priority_weights.get(test_case.get('priority', 'low'), 1)
        category_score = self.category_weights.get(test_case.get('category', 'functional'), 1)
        
        # Bonus for complex tests (more steps)
        steps = test_case.get('steps', [])
        complexity_bonus = min(len(steps) * 0.3, 2)
        
        # Bonus for error handling tests
        error_bonus = 1.5 if test_case.get('category') == 'error' else 1
        
        total_score = (priority_score * 0.4 + category_score * 0.3 + 
                      complexity_bonus * 0.2) * error_bonus
        
        return total_score