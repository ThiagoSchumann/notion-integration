import requests
from src.application.repositories.notion_repo import NotionRepository
from src.domain.entities.account_balance import AccountBalance
from config import Config

class NotionAdapter(NotionRepository):
    def get_account_balance(self) -> AccountBalance:
        headers = {
            'Authorization': f'Bearer {Config.NOTION_API_KEY}',
            'Notion-Version': Config.NOTION_VERSION,
            'Content-Type': 'application/json',
        }

        response = requests.post(Config.NOTION_API_URL, headers=headers, json={})
        data = response.json()
        
        if data.get("results"):
            page = data["results"][0]
            rollup = page["properties"].get("Rollup")
            if rollup and rollup["type"] == "rollup" and rollup["rollup"]["type"] == "number":
                total = rollup["rollup"]["number"]
                return AccountBalance(total)
        
        return AccountBalance(0.0)
