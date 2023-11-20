# When commit&push, trigger the jobs automatically
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Replace with your environment variables or provide the actual values
server_hostname = os.getenv("adb-7032072092481436.16.azuredatabricks.net")
job_id = os.getenv("736264284410811")
access_token = os.getenv("dapi078ded0930678a2d76aacdf05d5ff6fd-3")
url = f'https://{server_hostname}/api/2.0/jobs/run-now'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

data = {
    'job_id': job_id
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print('Job run successfully triggered')
else:
    print(f'Error: {response.status_code}, {response.text}')