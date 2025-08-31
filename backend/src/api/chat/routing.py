from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=ChatMessage | None, dependencies=[Depends(get_session)])
async def create_chat_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session),
) -> ChatMessage | None:
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    
    return obj


@router.get(
    "/recent/",
    response_model=list[ChatMessageListItem] | None,
    dependencies=[Depends(get_session)]
)
async def get_chat_messages(session: Session = Depends(get_session)) -> list[ChatMessageListItem] | None:
    results = session.exec(select(ChatMessage).order_by(ChatMessage.id.desc()).limit(10)).fetchall()
    return results
