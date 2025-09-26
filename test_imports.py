# Test all imports
try:
    import fastapi
    import uvicorn
    import selenium
    import webdriver_manager
    print(" All packages imported successfully!")
    
    # Test our agents
    from agents.planner import PlannerAgent
    from agents.ranker import RankerAgent
    from agents.executor import ExecutorAgent
    from agents.analyzer import AnalyzerAgent
    from agents.orchestrator import OrchestratorAgent
    print(" All agents imported successfully!")
    
    print("🎉 Everything works! Now run: python -m uvicorn main:app --reload")
    
except Exception as e:
    print(f" Import error: {e}")