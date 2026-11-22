"""Operations over in-memory support tickets."""

from collections.abc import Iterable

from customer_ops.models import Ticket


def filter_tickets_by_status(tickets: Iterable[Ticket], status: str) -> list[Ticket]:
    """Return tickets matching a status without changing the input."""
    return [ticket for ticket in tickets if ticket.status == status]


def sort_tickets_by_priority(tickets: Iterable[Ticket]) -> list[Ticket]:
    """Sort tickets by descending priority, then ascending ticket ID."""
    return sorted(tickets, key=lambda ticket: (-ticket.priority, ticket.ticket_id))
