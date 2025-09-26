# Test if all imports work
try:
    import time
    import os
    import json
    print("✅ Basic imports work!")
    
    from agents.analyzer import AnalyzerAgent
    print("✅ AnalyzerAgent imports work!")
    
    analyzer = AnalyzerAgent()
    test_result = {"test_id": 1, "status": "passed", "test_name": "Test"}
    validation = analyzer.validate_test(test_result)
    print("✅ AnalyzerAgent works!")
    print("Validation result:", validation)
    
except Exception as e:
    print("❌ Error:", e)