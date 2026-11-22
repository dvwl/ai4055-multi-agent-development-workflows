"""Print a tenant-scoped page from the synthetic capstone data."""

from customer_health.models import Account
from customer_health.repository import AccountRepository
from customer_health.service import list_accounts


def main() -> None:
    repository = AccountRepository(
        [
            Account(1, "north", "Amber Studio", "paused", 4, 0, 20),
            Account(2, "south", "Blue Harbor", "active", 12, 2, 40),
            Account(3, "north", "Cedar Works", "active", 0, 1, 3),
        ]
    )
    for account in list_accounts(repository, "north"):
        print(
            f"{account.account_id}: {account.display_name} "
            f"(status={account.status}, overdue_days={account.overdue_days})"
        )


if __name__ == "__main__":
    main()
