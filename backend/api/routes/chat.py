from fastapi import APIRouter

from schemas.chat_schema import ChatRequest

from services.chat_service import chat_service

router = APIRouter()


@router.post("/chat")
def chat(request: ChatRequest):

    return chat_service.ask(
        request.question,
        request.document_id
    )