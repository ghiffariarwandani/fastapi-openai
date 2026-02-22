import markdown
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates

from app.modules.coffee.prompt import SYSTEM_PROMPT
from app.utils.openai import client

coffee_router = APIRouter(prefix="/coffee", tags=["coffee"])

template = Jinja2Templates("templates")


@coffee_router.get("/")
def get_coffee(request: Request):
    return template.TemplateResponse("index.html", {"request": request})


@coffee_router.post("/")
def create_coffee(request: Request, topic=Form(None)):
    res = client.chat.completions.create(
        model="z-ai/glm-4.5-air:free",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": topic,
            },
        ],
    )

    result = res.choices[0].message.content

    html = markdown.markdown(result)

    return template.TemplateResponse(
        "index.html",
        {"request": request, "result": html, "user_input": topic},
    )
