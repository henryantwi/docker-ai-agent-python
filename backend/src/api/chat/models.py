from datetime import datetime, timezone
from sqlmodel import Field, SQLModel, DateTime


class ChatMessagePayload(SQLModel):
    # this is for validation
    message: str

class ChatMessage(SQLModel, table=True):
    # this is for database (i.e. saving, updating, deleting, getting, etc.)
    id: int | None = Field(default=None, primary_key=True)
    message: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now().replace(tzinfo=timezone.utc),
        sa_type=DateTime(timezone=True),
        primary_key=False,
        nullable=False,
    )
    

class ChatMessageListItem(SQLModel):
    message: str
    created_at: datetime = Field(default=None)
    