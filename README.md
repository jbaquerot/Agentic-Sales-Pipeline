# Sales Pipeline Automation

This project automates the sales pipeline process by scoring leads and generating personalized email content. It uses FastAPI for the web server, Pydantic for data validation, and various AI agents for lead scoring and email drafting.

## Features

- **Lead Scoring**: Automatically scores leads based on various criteria.
- **Email Drafting**: Generates personalized email content for qualified leads.
- **API Endpoints**: Provides a RESTful API to start the sales pipeline process.

## Requirements

- Python 3.8+
- FastAPI
- Pydantic
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/sales-pipeline-automation.git
    cd sales-pipeline-automation
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Set up the environment variables:
    ```sh
    cp .env.example .env  # Create a .env file from the example
    ```

4. Run the application:
    ```sh
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

## Usage

### Start the Pipeline

You can start the sales pipeline by sending a POST request to the `/start_pipeline/` endpoint with a JSON payload containing the lead data.

Example payload:
```json
{
    "leads": [
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
                "icp": "Enterprise companies.",
                "pitch": "American Company that Manufactures Everything."
            }
        }
    ]
}
```

## Run Tests
To run the tests, use the following command:
```sh
    pytest
```
# Project Structure
```
sales-pipeline-automation/
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── main.py
│   ├── lead_qualification.py
│   ├── email_engagement.py
│   ├── logging_config.py
│   └── errors.py
├── tests/
│   ├── test_routes.py
│   └── test_services.py
├── config/
│   ├── lead_qualification_agents.yaml
│   ├── lead_qualification_tasks.yaml
│   ├── email_engagement_agents.yaml
│   └── email_engagement_tasks.yaml
├── .env
├── .gitignore
├── requirements.txt
├── pytest.ini
└── README.md
```

# Contributing
Feel free to submit issues and enhancement requests.

# License
This project is licensed under the MIT License.

This README provides a clear overview of the project, its features, installation steps, usage instructions, project structure, and how to contribute.
