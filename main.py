from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


from typing import Annotated


template = Jinja2Templates('.')

app = FastAPI()


@app.get('/')
def index(request: Request, paste_code: str = None):
    if not paste_code:
        return template.TemplateResponse('index.html', {'request': request})
    ...

@app.post('/')
def create_paste(content: Annotated[str, Form()]):
    with open('asd', 'w') as file:
        print(content, file=file)


if __name__ == '__main__':
    import uvicorn


    uvicorn.run('main:app', reload=True)
