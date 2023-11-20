from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"messeage":"welcome "}


@app.get("/chat/{user_question}")
async def get_response(user_question: str):
    return user_question





