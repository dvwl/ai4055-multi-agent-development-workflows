# Example service layout

Proposed service name: `notification_preferences`

## Responsibilities

- Store a user's notification preferences.
- Validate requested channels against the application's supported channel list.
- Return a user's current preferences without exposing credentials or message content.

## Boundaries

- The API layer validates request shape and maps errors to the existing response contract.
- The service layer owns preference rules.
- Persistence implementation is not selected in this exercise; identify the current repository pattern before proposing one.
- Tests must cover valid updates, unsupported channels, missing users, and unchanged state after rejected input.

## Out of scope

- Sending notifications.
- Adding a new database or external provider.
- Changing authentication or authorization policy.
- Implementing the service during the planning lab.
