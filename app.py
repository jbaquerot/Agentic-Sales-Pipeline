# app.py
import logging
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from src.lead_qualification import SalesPipeline, LeadsRequest

# Load environment variables from .env file
load_dotenv()

# Configure logging
#logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Routes
router = APIRouter()

@router.post("/start_pipeline/")
async def start_pipeline(leads_request: LeadsRequest):
    try:
        logger.info("Starting pipeline with leads: %s", leads_request)
        flow = SalesPipeline(leads_request.leads)
        emails = await flow.kickoff_async()
        print(emails)
        logger.info("Pipeline completed successfully")
        return emails
    except HTTPException as e:
        logger.error("HTTPException occurred: %s", e.detail)
        raise e
    except Exception as e:
        logger.error("An unexpected error occurred: %s", e)
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    host = os.getenv('APP_HOST', '0.0.0.0')
    port = int(os.getenv('APP_PORT', 8000))
    uvicorn.run(app, host=host, port=port, reload=True)
