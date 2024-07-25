from abc import ABC, abstractmethod
from src.domain.entities.account_balance import AccountBalance

class NotionRepository(ABC):
    @abstractmethod
    def get_account_balance(self) -> AccountBalance:
        pass
