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
        print(" Starting multi-agent testing suite...")
        orchestrator = OrchestratorAgent()
        report = orchestrator.run_full_test_suite()
        
        return {
            "status": "success",
            "message": "Multi-agent testing completed successfully!",
            "report": report
        }
    except Exception as e:
        error_msg = f"Testing failed: {str(e)}"
        print(f" {error_msg}")
        return {
            "status": "error",
            "message": error_msg,
            "report": None
        }

@app.get("/api/report")
async def get_report():
    try:
        with open("artifacts/comprehensive_test_report.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"error": "No report available. Please run tests first."}

app.mount("/", StaticFiles(directory="frontend"), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)