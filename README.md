# PasswordGenerator
Password generation app using Svelte and FastAPI. 

* Generate passwords of 8 to 128 characters by a browser.
* The characters used are A-Z / a-z (default).
* Optionally specify numbers (0-9) and punctuation.
* Specify any text you want.
* Currently, you can also input double-byte characters such as Japanese.

# Requirements

Frontend: npm or yarn

```sh
cd PasswordGenarator
yarn install
yarn run dev
```

Backend: Python 3.9+, Poetry

```sh
cd PasswordGenarator/api
poetry install
poetry shell
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

**Note**: Wrote "pynvim" in pyproject.toml. It is for the defx plugin.

**Note**: My backend env is Ubuntu on Parallels. So, it starts with 0.0.0.0:8000 to request from Svelte (macOS). Would you please start uvicorn according to the env you are going to try?

# Motivation

To use Python's "secrets" lib for password generation, I decided to use them. Generally, you wouldn't need to communicate with a server to generate a password. I wanted to use a secure random number to create it.
