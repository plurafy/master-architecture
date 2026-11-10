"""
The State Design Pattern is a behavioral design pattern that allows an object to completely alter its behavior when its internal state changes. To the outside world, it appears as if the object has dynamically changed its class.

Instead of cluttering a single class with massive if-elif-else or match-case blocks to handle different statuses, the behavior for each state is encapsulated into its own distinct class.

Here is a complete, clean Python implementation modeling a Document workflow (Draft → Moderation → Published).
"""

from abc import ABC, abstractmethod


class State(ABC):
    @property
    def context(self) -> "Document":
        return self._context

    @context.setter
    def context(self, context: "Document") -> None:
        self._context = context

    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def publish(self) -> None:
        pass


class Document:
    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """Allows dynamically changing the state at runtime."""
        self._state = state
        self._state.context = self

    def render(self):
        self._state.render()

    def publish(self):
        self._state.publish()


class DraftState(State):
    def render(self):
        print("Draft State: Showing document edit mode.")

    def publish(self) -> None:
        print("Draft State: Moving document to moderation.")
        self.context.transition_to(ModerationState())


class ModerationState(State):
    def render(self):
        print("Moderation State: Rendering readonly view with review tools.")

    def publish(self) -> None:
        print("Moderation State: Moving document to published.")
        self.context.transition_to(PublishedState())


class PublishedState(State):
    def render(self):
        print("PublishedState State: Rendering public view.")

    def publish(self) -> None:
        print("PublishedState State: Already Published!")


if __name__ == "__main__":
    # Start as a Draft
    doc = Document(DraftState())

    doc.render()  # Output: Draft State: Showing document edit mode.
    doc.publish()  # Output: Draft State: Moving document to moderation.

    print("-" * 10)

    doc.render()  # Output: Moderation State: Showing read-only view...
    doc.publish()  # Output: Moderation State: Approving and publishing...

    print("-" * 10)

    doc.render()  # Output: Published State: Rendering publicly available page.
    doc.publish()  # Output: Published State: Already published. Doing nothing.
