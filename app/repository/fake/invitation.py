from typing import List, Optional, Self

from app.model.domain import Invitation
from app.repository.invitation import IInvitationRepository


class FakeInvitationRepository(IInvitationRepository):
    def __init__(self: Self) -> None:
        self.data: dict[int, Invitation] = {}
        self.counter: int = 1

    def add(self: Self, record: Invitation) -> Invitation:
        record.id = self.counter

        self.data[self.counter] = record
        self.counter += 1

        return record

    def update(self: Self, record: Invitation) -> None:
        if record.id in self.data:
            self.data[record.id] = record

    def delete(self: Self, record: Invitation) -> None:
        if record.id in self.data:
            del self.data[record.id]

    def get_all(self: Self) -> List[Invitation]:
        return list(self.data.values())

    def get_by_id(self: Self, id: int) -> Optional[Invitation]:
        return self.data.get(id)
