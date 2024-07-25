import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    NOTION_API_URL = os.getenv('NOTION_API_URL')
    NOTION_API_KEY = os.getenv('NOTION_API_KEY')
    NOTION_VERSION = os.getenv('NOTION_VERSION')
