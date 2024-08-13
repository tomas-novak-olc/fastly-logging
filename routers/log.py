import json

from fastapi import Request
from fastapi.routing import APIRouter

from models.log import LogEntry

router = APIRouter()


@router.post("/log/")
async def log(request: Request):
    body = await request.body()
    text = body.decode("utf-8")

    data = [LogEntry(**i) for i in json.loads(text)]

    await LogEntry.bulk_create(data)
