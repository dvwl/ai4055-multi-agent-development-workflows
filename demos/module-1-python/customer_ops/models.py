"""Data models for the ticket-service demo."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Ticket:
    ticket_id: int
    title: str
    status: str
    priority: int
