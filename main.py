from fastapi import FastAPI
import uvicorn
import pyjokes
import wikipedia
from pydantic import BaseModel

app = FastAPI()
wikipedia.set_lang('ru')


class Wiki(BaseModel):
    question: str
    result: int = 4


# @app.get("/")
# def joke():
#     return pyjokes.get_joke()
#
#
# @app.get("/{friend}")
# def friends_joke(friend: str):
#     return friend + " tells his joke:" + pyjokes.get_joke()
#
#
# @app.get("/multi/{friend}")
# def multi_friends_joke(friend: str, jokes_number: int):
#     result = ""
#     for i in range(jokes_number):
#         result += friend + f"tells his joke #{i + 1}:" + pyjokes.get_joke() + ""
#     return result


#
# class Joke(BaseModel):
#     friend: str
#     joke: str
#
# class JokeInput(BaseModel):
#     friend: str
#
# @app.post("/")
# def create_joke(joke_input: JokeInput):
#     return Joke(friend=joke_input.friend + ", tell me joke", joke=pyjokes.get_joke())


# ср


@app.get("/wiki/{question}")
def question_wikipedia(question: str):
    return wikipedia.search(question)


@app.get("/wiki/article/{question}")
def article_question_wikipedia(question: str, result: int = 4):
    return wikipedia.summary(question, sentences=result), wikipedia.page(question).url


@app.post("/")
def wikipedia_search(w_search: Wiki):
    return wikipedia.search(w_search.question, results=w_search.result)


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
