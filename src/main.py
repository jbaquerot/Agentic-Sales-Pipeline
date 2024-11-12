import asyncio
from lead_qualification import SalesPipeline
import logging

# Logging
logger = logging.getLogger(__name__)

async def main():
    leads = [
            {
                "lead_data": {
                    "name": "João Moura",
                    "job_title": "Director of Engineering",
                    "company": "Clearbit",
                    "email": "joao@clearbit.com",
                    "use_case": "Using AI Agent to do better data enrichment."
                },
                "our_data": {
                    "company_name": "GMV",
                    "product": "AI Solutions",
                    "icp": "Enterprise companies.",
                    "pitch": "AI for smarter decision making."
                },
            },
            
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
