import requests
import json
import time
def collect_tweets():
    # Step 1: Trigger Data Collection
    api_url_trigger = "https://api.brightdata.com/datasets/v3/trigger?dataset_id=gd_lwxkxvnf1cynvib9co&include_errors=true&type=discover_new&discover_by=profile_url"
    api_token = "YOUR_API_TOKEN"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    payload = [
        {
            "url": "https://x.com/elonmusk",
            "start_date": "2024-03-15T16:31:04.000Z",
            "end_date": "2024-05-15T22:00:06.000Z"
        }
    ]

    response = requests.post(api_url_trigger, headers=headers, data=json.dumps(payload))
    data = response.json()
    snapshot_id = data.get("snapshot_id")
    print(f"Snapshot ID: {snapshot_id}")

    # Step 2: Retrieve Data
    api_url_retrieve = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"

    while True:
        response = requests.get(api_url_retrieve, headers=headers)
        data = response.json()
        if data.get("status") == "running":
            print("Snapshot is not ready yet, trying again in 10 seconds...")
            time.sleep(10)
        else:
            print("Data retrieved:")
            print(data)
            break

collect_tweets()