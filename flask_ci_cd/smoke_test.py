import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("APP_URL")

def test_main_app_health():
    print(f"Cheking main app health")
    r = requests.get(f"{base_url}/health")
    assert r.status_code == 200
    print("Health check passed")


if __name__=='__main__':
    test_main_app_health()