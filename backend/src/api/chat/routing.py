from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem
from api.db import get_session
from api.ai.agents import get_supervisor
from api.ai.services import generate_email_message
from api.ai.schemas import EmailMessageSchema, SupervisorMessageSchema


router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=SupervisorMessageSchema | None, dependencies=[Depends(get_session)])
async def create_chat_message(
    payload: ChatMessagePayload,
    session: Session = Depends(get_session),
) -> SupervisorMessageSchema | None:
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    supe = get_supervisor()
    msg_data = {
        "messages": [
            {
                "role": "user", 
                "content": f"{payload.message}"
            },
        ]
    }
    response = supe.invoke(msg_data)
    if not response:
        raise HTTPException(status_code=500, detail="No response from supervisor")
    messages = response.get("messages")
    if not messages:
        raise HTTPException(status_code=500, detail="No messages from supervisor")
    return messages[-1]


@router.get(
    "/recent/",
    response_model=list[ChatMessageListItem] | None,
    dependencies=[Depends(get_session)]
)
async def get_chat_messages(session: Session = Depends(get_session)) -> list[ChatMessageListItem] | None:
    results = session.exec(select(ChatMessage).order_by(ChatMessage.id.desc()).limit(10)).fetchall()
    return results
