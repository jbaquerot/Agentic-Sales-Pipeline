# client.py
import requests
import json

def send_post_request(url, payload):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    url = "http://127.0.0.1:8000/start_pipeline/"
    payload = {
        "leads": [
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
                }
            }
        ]
    }

    try:
        result = send_post_request(url, payload)
        print("Response from server:", result)
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
