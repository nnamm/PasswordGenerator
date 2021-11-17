import secrets
import string

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

origins = ["http://localhost", "http://localhost:5000"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequestBody(BaseModel):
    passwd_chars: int
    request_digit: bool
    request_punctuation: bool
    specified_text: str


@app.post("/gen_passwd/")
async def generate_passwd(req: RequestBody):
    if len(req.specified_text) > 0:
        letters = req.specified_text
    else:
        letters = string.ascii_letters
        if req.request_digit:
            letters += string.digits
        if req.request_punctuation:
            letters += string.punctuation

    return {"Passwd": "".join(secrets.choice(letters) for _ in range(req.passwd_chars))}
