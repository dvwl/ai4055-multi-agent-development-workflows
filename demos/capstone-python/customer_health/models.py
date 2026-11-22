"""Domain model for synthetic customer account records."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    account_id: int
    tenant_id: str
    display_name: str
    status: str
    overdue_days: int
    open_issue_count: int
    last_activity_days: int
