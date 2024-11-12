# tests/test_routes.py
import pytest
from fastapi.testclient import TestClient
from app import app
from src.models import LeadsRequest, Lead

client = TestClient(app)

def test_start_pipeline_success():
    lead_data = {"lead_data": {"name": "John Doe"}, "our_data": {"company": "Example Corp"}}
    leads_request = LeadsRequest(leads=[Lead(**lead_data)])

    response = client.post("/start_pipeline/", json=leads_request.dict())

    assert response.status_code == 200
    assert "emails" in response.json()

def test_start_pipeline_invalid_data():
    invalid_lead_data = {"lead_data": "Invalid data", "our_data": {"company": "Example Corp"}}
    leads_request = LeadsRequest(leads=[Lead(**invalid_lead_data)])

    response = client.post("/start_pipeline/", json=leads_request.dict())

    assert response.status_code == 422  # Unprocessable Entity

def test_start_pipeline_internal_error():
    lead_data = {"lead_data": {"name": "John Doe"}, "our_data": {"company": "Example Corp"}}
    leads_request = LeadsRequest(leads=[Lead(**lead_data)])

    # Mock the kickoff_async method to raise an exception
    def mock_kickoff_async(self):
        raise Exception("Mocked error")

    from src.lead_qualification import SalesPipeline
    SalesPipeline.kickoff_async = mock_kickoff_async

    response = client.post("/start_pipeline/", json=leads_request.dict())

    assert response.status_code == 500
    assert "error" in response.json()
