import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
server_h = os.getenv("SERVER_HOSTNAME")
access_token = os.getenv("TOKEN")
FILESTORE_PATH = "dbfs:/FileStore/individual_project3"
# headers = {"Authorization": "Bearer %s" % access_token}
url = "https://"+server_h+"/api/2.0"

def check_filestore_path(path, headers): 
    try:
        response = requests.get(url + f"/dbfs/get-status?path={path}", headers=headers)
        response.raise_for_status()
        return response.json()['path'] is not None
    except Exception as e:
        print(f"Error checking file path: {e}")
        return False

# Test if the specified FILESTORE_PATH exists
def test_databricks():
    headers = {'Authorization': f'Bearer {access_token}'}
    assert check_filestore_path(FILESTORE_PATH, headers) is True

if __name__ == "__main__":
    test_databricks()