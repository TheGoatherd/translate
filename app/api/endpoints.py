from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq   

# make an input validation class
class Schema(BaseModel):
    query: str

# load environment variables from .env file
load_dotenv()
client= Groq(api_key=os.getenv("API_KEY"))

app = FastAPI()

app.post("/chutpaglu") 
async def chutpaglu(data: Schema):
    completion = client.chat.completions.create(
        model="llama-3.2-90b-vision-preview",
        messages=[{"role": "user", "content": f"Translate in Hindi  : {data.query}"}],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False
    )

    answer = completion.choices[0].message.content if completion.choices else None
    return {"answer": answer}