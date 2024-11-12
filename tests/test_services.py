# tests/test_services.py
import pytest
from src.lead_qualification import run_main, run_pipeline
from src.models import Lead, LeadsRequest
from src.errors import KickoffError, ValidationError

@pytest.mark.asyncio
async def test_run_main_success():
    lead_data = {"lead_data": {"name": "John Doe"}, "our_data": {"company": "Example Corp"}}
    leads = [Lead(**lead_data)]

    # Mock the kickoff_async method to return a successful result
    class MockSalesPipeline:
        async def kickoff_async(self):
            return ["email1@example.com", "email2@example.com"]

    from src.lead_qualification import SalesPipeline
    SalesPipeline = MockSalesPipeline

    emails = await run_main(leads)

    assert len(emails) == 2
    assert "email1@example.com" in emails
    assert "email2@example.com" in emails

@pytest.mark.asyncio
async def test_run_main_kickoff_error():
    lead_data = {"lead_data": {"name": "John Doe"}, "our_data": {"company": "Example Corp"}}
    leads = [Lead(**lead_data)]

    # Mock the kickoff_async method to raise a KickoffError
    class MockSalesPipeline:
        async def kickoff_async(self):
            raise KickoffError("Mocked KickoffError")

    from src.lead_qualification import SalesPipeline
    SalesPipeline = MockSalesPipeline

    with pytest.raises(KickoffError):
        await run_main(leads)

@pytest.mark.asyncio
async def test_run_pipeline_success():
    lead_data = {"lead_data": {"name": "John Doe"}, "our_data": {"company": "Example Corp"}}
    leads_request = LeadsRequest(leads=[Lead(**lead_data)])

    # Mock the run_main function to return a successful result
    class MockRunMain:
        async def __call__(self, leads):
            return ["email1@example.com", "email2@example.com"]

    from src.lead_qualification import run_main
    run_main = MockRunMain()

    result = await run_pipeline(leads_request)

    assert "emails" in result
    assert len(result["emails"]) == 2
    assert "email1@example.com" in result["emails"]
    assert "email2@example.com" in result["emails"]

@pytest.mark.asyncio
async def test_run_pipeline_validation_error():
    lead_data = {"lead_data": "Invalid data", "our_data": {"company": "Example Corp"}}
    leads_request = LeadsRequest(leads=[Lead(**lead_data)])

    with pytest.raises(ValidationError):
        await run_pipeline(leads_request)
