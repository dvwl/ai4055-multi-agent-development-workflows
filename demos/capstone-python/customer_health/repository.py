"""In-memory repository containing synthetic capstone records."""

from collections.abc import Iterable

from customer_health.models import Account


class AccountRepository:
    def __init__(self, accounts: Iterable[Account]) -> None:
        self._accounts = tuple(accounts)

    def list_for_tenant(self, tenant_id: str) -> list[Account]:
        """Return a new list of accounts for one tenant."""
        return [account for account in self._accounts if account.tenant_id == tenant_id]
