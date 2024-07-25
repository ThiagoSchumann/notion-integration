from flask import Blueprint, jsonify
from src.application.use_cases.notion.get_account_balance_use_case import GetAccountBalanceUseCase
from src.infra.notion.notion_adapter import NotionAdapter

notion_bp = Blueprint('notion', __name__)

@notion_bp.route('/account-balance', methods=['GET'])
def get_account_balance():
    use_case = GetAccountBalanceUseCase(NotionAdapter())
    account_balance = use_case.execute()
    return jsonify({"account_balance": account_balance.total})
