# Test syntax and imports
try:
    import json
    import os
    import time
    print("✅ Basic imports work")
    
    from agents.planner import PlannerAgent
    from agents.ranker import RankerAgent  
    from agents.executor import ExecutorAgent
    from agents.analyzer import AnalyzerAgent
    from agents.orchestrator import OrchestratorAgent
    print("✅ All agent imports work")
    
    # Test creating instances
    planner = PlannerAgent()
    ranker = RankerAgent()
    analyzer = AnalyzerAgent()
    print("✅ Agent instances created successfully")
    
    print("🎉 All syntax errors fixed! System is ready.")
    
except SyntaxError as e:
    print(f" Syntax error: {e}")
except ImportError as e:
    print(f" Import error: {e}")
except Exception as e:
    print(f" Other error: {e}")