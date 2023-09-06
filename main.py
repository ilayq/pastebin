from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from typing import Annotated
from hashlib import sha256

from db import sqliteDB


template = Jinja2Templates('.')
db = sqliteDB()
app = FastAPI()


@app.get('/')
async def index(request: Request, paste_code: str = None):
    if not paste_code:
        return template.TemplateResponse('index.html', {"value": '', 'request': request})
    else:
        content = db.get_paste(contenthash=paste_code)
        return template.TemplateResponse('index.html', {"value": content, 'request': request})


@app.post('/')
async def create_paste(content: Annotated[str, Form()]):
    contenthash = sha256(content.encode())
    if db.add_paste(contenthash=contenthash.hexdigest(), content=content):
        return RedirectResponse(f'/?paste_code={contenthash.hexdigest()}', status_code=302)
    return False


if __name__ == '__main__':
    import uvicorn


    uvicorn.run('main:app', port=80, host='0.0.0.0')
