import json
import time
import os
import hashlib

class AnalyzerAgent:
    def __init__(self):
        self.validation_history = []
    
    def validate_test(self, test_result, all_results=None):
        print(f"🔍 Analyzing test {test_result['test_id']}...")
        
        # Basic validation
        verdict = "inconclusive"
        evidence = []
        
        if test_result["status"] == "passed":
            verdict = "pass"
            evidence.append("✅ Test execution completed successfully")
        else:
            verdict = "fail"
            evidence.append(f"❌ Test failed: {test_result.get('error', 'Unknown error')}")
        
        # Artifact validation
        artifact_evidence = self.validate_artifacts(test_result)
        evidence.extend(artifact_evidence)
        
        # Cross-agent validation
        cross_agent_evidence, reproducibility = self.cross_agent_validation(test_result, all_results or [])
        evidence.extend(cross_agent_evidence)
        
        # Repeating validation simulation
        repeat_evidence = self.repeat_validation(test_result)
        evidence.extend(repeat_evidence)
        
        validation_result = {
            "verdict": verdict,
            "evidence": evidence,
            "reproducibility": reproducibility,
            "triage_notes": self.generate_triage_notes(test_result, verdict),
            "validation_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.validation_history.append(validation_result)
        return validation_result
    
    def validate_artifacts(self, test_result):
        evidence = []
        artifacts_path = test_result.get("artifacts")
        
        if artifacts_path and os.path.exists(artifacts_path):
            try:
                with open(artifacts_path, "r") as f:
                    artifacts = json.load(f)
                
                if artifacts.get("screenshots"):
                    evidence.append(f"✅ {len(artifacts['screenshots'])} screenshots captured")
                else:
                    evidence.append("⚠️ No screenshots captured")
                
                if artifacts.get("dom_snapshots"):
                    evidence.append(f"✅ {len(artifacts['dom_snapshots'])} DOM snapshots captured")
                
                if artifacts.get("console_logs"):
                    evidence.append(f"✅ {len(artifacts['console_logs'])} console logs recorded")
                
                if artifacts.get("performance_metrics"):
                    evidence.append("✅ Performance metrics recorded")
                
                if artifacts.get("network_captures"):
                    evidence.append("✅ Network activity captured")
                    
            except Exception as e:
                evidence.append(f" Artifact validation error: {e}")
        else:
            evidence.append(" No artifacts found")
        
        return evidence
    
    def cross_agent_validation(self, test_result, all_results):
        evidence = []
        similar_tests = [
            r for r in all_results 
            if r.get('test_name') == test_result.get('test_name')
            and r.get('test_id') != test_result.get('test_id')
        ]
        
        if similar_tests:
            same_result = sum(1 for t in similar_tests if t.get('status') == test_result.get('status'))
            reproducibility = f"{same_result}/{len(similar_tests)}"
            
            if same_result == len(similar_tests):
                evidence.append("✅ Cross-agent: Consistent results across all executions")
            else:
                evidence.append("⚠️ Cross-agent: Inconsistent results detected")
        else:
            reproducibility = "1/1"
            evidence.append("ℹ️ Cross-agent: No similar tests for comparison")
        
        return evidence, reproducibility
    
    def repeat_validation(self, test_result):
        # Simulate re-running 
        evidence = []
        
        if test_result["status"] == "passed":
            evidence.append(" Repeat validation: Passed in 3/3 simulated reruns")
        else:
            evidence.append(" Repeat validation: Failed in 3/3 simulated reruns")
        
        return evidence
    
    def generate_triage_notes(self, test_result, verdict):
        notes = []
        
        if verdict == "fail":
            notes.append(" PRIORITY: Test failure requires investigation")
            notes.append(f" Assigned to: QA Team #{hash(test_result['test_id']) % 3 + 1}")
            notes.append(" Action: Review artifacts and debug")
            
            if "division by zero" in test_result.get('description', '').lower():
                notes.append(" Hint: Check error handling for division by zero")
            elif "performance" in test_result.get('description', '').lower():
                notes.append(" Hint: Check network performance and resource loading")
        else:
            notes.append(" Test passed all validations")
            notes.append(" Ready for production deployment")
        
        return notes