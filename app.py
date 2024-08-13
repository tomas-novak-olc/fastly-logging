from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from tortoise.contrib.fastapi import register_tortoise

from routers import log

app = FastAPI()

with open("fastly_tokens.txt", "r") as f:
    fastly_tokens = f.read().splitlines()
    SHA_TOKENS = "\n".join(fastly_tokens)


@app.get("/")
def index():
    return "Logging server"


@app.get("/.well-known/fastly/logging/challenge")
def challenge():
    return HTMLResponse(SHA_TOKENS)


app.include_router(log.router, prefix="/api")

register_tortoise(
    app,
    db_url="asyncpg://postgres:postgres@localhost:5432/postgres",
    modules={"models": ["models.log"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
