from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from agents.orchestrator import OrchestratorAgent
import os
import json

app = FastAPI(title="Multi-Agent Game Tester POC")

@app.get("/")
async def read_root():
    return FileResponse('frontend/index.html')

@app.get("/api/start-testing")
async def start_testing():
    try:
        print("🎯 Starting multi-agent testing suite...")
        orchestrator = OrchestratorAgent()
        report = orchestrator.run_full_test_suite()
        
        # Ensure the report has the expected structure
        if report and 'summary' in report:
            return {
                "status": "success",
                "message": "Multi-agent testing completed successfully!",
                "report": report
            }
        else:
            return {
                "status": "error",
                "message": "Report generation failed",
                "report": None
            }
            
    except Exception as e:
        error_msg = f"Testing failed: {str(e)}"
        print(f"❌ {error_msg}")
        return {
            "status": "error",
            "message": error_msg,
            "report": None
        }

@app.get("/api/report")
async def get_report():
    try:
        with open("artifacts/comprehensive_test_report.json", "r", encoding="utf-8") as f:
            report = json.load(f)
            return {
                "status": "success",
                "report": report
            }
    except Exception as e:
        return {
            "status": "error", 
            "message": f"No report available: {str(e)}"
        }

app.mount("/", StaticFiles(directory="frontend"), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
