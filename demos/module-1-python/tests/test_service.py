import unittest

from customer_ops.models import Ticket
from customer_ops.service import filter_tickets_by_status, sort_tickets_by_priority


class TicketServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tickets = [
            Ticket(3, "Replace access card", "open", 2),
            Ticket(1, "Restore account", "open", 3),
            Ticket(2, "Update contact details", "closed", 3),
            Ticket(4, "Reset password", "open", 1),
        ]

    def test_filter_tickets_by_status(self) -> None:
        self.assertEqual(
            [3, 1, 4],
            [ticket.ticket_id for ticket in filter_tickets_by_status(self.tickets, "open")],
        )

    def test_filter_returns_empty_list_when_status_has_no_matches(self) -> None:
        self.assertEqual([], filter_tickets_by_status(self.tickets, "pending"))

    def test_sort_tickets_by_priority_then_ticket_id(self) -> None:
        self.assertEqual(
            [1, 2, 3, 4],
            [ticket.ticket_id for ticket in sort_tickets_by_priority(self.tickets)],
        )

    def test_sort_does_not_change_input_order(self) -> None:
        original_ids = [ticket.ticket_id for ticket in self.tickets]

        sort_tickets_by_priority(self.tickets)

        self.assertEqual(original_ids, [ticket.ticket_id for ticket in self.tickets])


if __name__ == "__main__":
    unittest.main()
