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

    try:
        result = send_post_request(url, payload)
        print("Response from server:", result)
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
