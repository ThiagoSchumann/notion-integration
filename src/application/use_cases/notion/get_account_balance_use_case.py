from src.application.repositories.notion_repo import NotionRepository
from src.domain.entities.account_balance import AccountBalance

class GetAccountBalanceUseCase:
    def __init__(self, notion_repository: NotionRepository):
        self.notion_repository = notion_repository
    
    def execute(self) -> AccountBalance:
        return self.notion_repository.get_account_balance()
