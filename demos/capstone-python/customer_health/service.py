"""Application service for the capstone's existing account-list behavior."""

from customer_health.models import Account
from customer_health.repository import AccountRepository

MAX_PAGE_SIZE = 50
VALID_STATUSES = frozenset({"active", "paused", "closed"})


def list_accounts(
    repository: AccountRepository,
    tenant_id: str,
    *,
    status: str | None = None,
    offset: int = 0,
    limit: int = 20,
) -> list[Account]:
    """Return a bounded, tenant-scoped page of accounts.

    This baseline does not define account-health thresholds; see feature-request.md.
    """
    if not tenant_id.strip():
        raise ValueError("tenant_id is required")
    if status is not None and status not in VALID_STATUSES:
        raise ValueError("status is not supported")
    if offset < 0:
        raise ValueError("offset must be non-negative")
    if limit < 1 or limit > MAX_PAGE_SIZE:
        raise ValueError(f"limit must be between 1 and {MAX_PAGE_SIZE}")

    accounts = repository.list_for_tenant(tenant_id)
    if status is not None:
        accounts = [account for account in accounts if account.status == status]
    accounts.sort(key=lambda account: account.account_id)
    return accounts[offset : offset + limit]
