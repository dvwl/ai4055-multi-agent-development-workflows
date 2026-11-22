import unittest

from customer_health.models import Account
from customer_health.repository import AccountRepository
from customer_health.service import list_accounts


class ListAccountsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = AccountRepository(
            [
                Account(3, "north", "Cedar Works", "active", 0, 1, 3),
                Account(1, "north", "Amber Studio", "paused", 4, 0, 20),
                Account(2, "south", "Blue Harbor", "active", 12, 2, 40),
            ]
        )

    def test_lists_only_the_requested_tenant_in_stable_order(self) -> None:
        result = list_accounts(self.repository, "north")

        self.assertEqual([1, 3], [account.account_id for account in result])

    def test_filters_by_status_before_pagination(self) -> None:
        result = list_accounts(self.repository, "north", status="active", limit=1)

        self.assertEqual([3], [account.account_id for account in result])

    def test_rejects_invalid_status(self) -> None:
        with self.assertRaises(ValueError):
            list_accounts(self.repository, "north", status="unknown")

    def test_rejects_unbounded_or_invalid_pagination(self) -> None:
        for offset, limit in [(-1, 10), (0, 0), (0, 51)]:
            with self.subTest(offset=offset, limit=limit):
                with self.assertRaises(ValueError):
                    list_accounts(self.repository, "north", offset=offset, limit=limit)

    def test_rejects_empty_tenant_scope(self) -> None:
        with self.assertRaises(ValueError):
            list_accounts(self.repository, " ")


if __name__ == "__main__":
    unittest.main()
