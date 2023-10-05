from fastapi import FastAPI
import uvicorn
import pyjokes
import wikipedia
from pydantic import BaseModel

app = FastAPI(title='labawiki')
wikipedia.set_lang('ru')


class Wiki(BaseModel):
    question: str
    result: int = 4


class Answer(BaseModel):
    answer: list[str]


class Article(BaseModel):
    Question: str
    Summary: str
    URL: str


class WQuestion(BaseModel):
    Ques1: list[str]


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

# path
@app.get("/wiki/{question}", response_model=WQuestion)
def question_wikipedia(question: str):
    return WQuestion(Ques1=wikipedia.search(question)
                     )


# path and querty
@app.get("/wiki/article/{question}", response_model=Article)
def article_question_wikipedia(question: str, result: int = 4):
    return Article(Question=question,
                   Summary=str(wikipedia.summary(question, sentences=result)),
                   URL=str(wikipedia.page(question).url)

                   )


# body
@app.post("/", response_model=Answer)
def wikipedia_search(w_search: Wiki):
    return Answer(answer=wikipedia.search(w_search.question, results=w_search.result)
                  )


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
