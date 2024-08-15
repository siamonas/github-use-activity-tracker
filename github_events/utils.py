import os
from dotenv import load_dotenv

def get_token():
    load_dotenv()
    return os.getenv("GITHUB_TOKEN")