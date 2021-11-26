"""Password Generator API"""

import random
from datetime import datetime
from string import ascii_letters, digits, punctuation

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .utils.utils import create_random_chars

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
    """RequestBody struct"""

    passwd_length: int
    digits_length: int
    symbols_length: int
    input_text: str
    is_include_today: bool


@app.post("/gen_passwd/")
async def generate_passwd(req: RequestBody):
    """Generate a password according to the parameters.

    This function works using alphabets(string.ascii_letters) by default.
    In the case of "Specify digits length", works using digits(string.digits).  In the
    case of "Specify symbols length", works using symbols(string.punctuation). Each will
    contain the specified length of digits/symbols.
    In the case of "Input text", works using inputted text.

    Args:
        req (RequestBody): Parameters from Frontend.

    Returns:
        Password formatted dict or "None".

    """

    if req.passwd_length == 0:
        return {"Passwd": "None"}

    # Input text & Today flag
    if req.is_include_today:
        today = datetime.now().strftime("%m%d")
        pw_chars = create_random_chars(req.input_text, req.passwd_length - len(today))
        return {"Passwd": pw_chars + today}

    # Input text
    if len(req.input_text) > 0:
        return {"Passwd": create_random_chars(req.input_text, req.passwd_length)}

    # Only alphabet
    if not req.digits_length and not req.symbols_length:
        return {"Passwd": create_random_chars(ascii_letters, req.passwd_length)}

    # Alphabet or Digits or Symbols
    if req.digits_length or req.symbols_length:
        tmp_length = req.passwd_length
        digits_symbols = ""

        if req.digits_length:
            digits_symbols += create_random_chars(digits, req.digits_length)
            tmp_length -= req.digits_length
        if req.symbols_length:
            digits_symbols += create_random_chars(punctuation, req.symbols_length)
            tmp_length -= req.symbols_length
        alphabet = create_random_chars(ascii_letters, tmp_length)

        pw_chars = random.sample((alphabet + digits_symbols), req.passwd_length)
        return {"Passwd": "".join(pw_chars)}
