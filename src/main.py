import asyncio
from lead_qualification import SalesPipeline
import logging

# Logging
logger = logging.getLogger(__name__)

async def main():
    leads = [
        {
            "lead_data": {
                "name": "Wile E. Coyote",
                "job_title": "Genius",
                "company": "Self-employed",
                "email": "wile_coyote@gmail.com",
                "use_case": "Using AI to fetch Road Runner."
            },
            "our_data": {
                "company_name": "Acme Corporation",
                "product": "The company manufactures outlandish products that fail or backfire catastrophically at the worst possible times",
                "icp": "Self-employed",
                "pitch": "American Company that Manufactures Everything."
            }
        }
            
        ]

    try:
        flow = SalesPipeline(leads)
        emails = await flow.kickoff_async()
        print(emails)
    except Exception as e:
        print(f"Error en kickoff_async: {e}")


if __name__ == "__main__":
    logger.info('Inicio main')
    asyncio.run(main())
