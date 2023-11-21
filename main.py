from load_meta_data import ChatBot

from enum import Enum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class Repo_ID(Enum):
    chat_model: str = "Mohammed-Altaf/medical_chatbot-8bit"


app = FastAPI()
bot = ChatBot()

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], 
    allow_credentials=True, 
    allow_methods=['*'], 
    allow_headers=['*'],
)

# load the model asynchronously on startup
@app.on_event("startup")
async def startup():
    bot.load_from_hub(Repo_ID.chat_model.value)

@app.get("/")
async def home():
    "Home route for the api"
    return {"messeage":"welcome, Application Successfully Loaded!!"}

# dummy test route
@app.get("/test_response/{query}")
async def test_inference(query:str):
    return query


@app.get("/query/{user_query}")
async def inference_output(user_query: str) -> str:
    """Main query route for the api, which return the response from the inference of the LanguageModel
    
    Keyword arguments:
    user_query -- Input string from the user, which is the question(input) to the Model
    Return: return's the response got from the Language model
    """
    
    global bot
    response = bot.get_response(user_query)
    return response

