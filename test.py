from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse


app = FastAPI()

@app.get("/message")
async def test_endpoint():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>hello</h1>
    </body>
    </html>
    """)


@app.get("/redirect")
async def redirect_endpoint(url: str):
    return HTMLResponse(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Redirecting...</title>
        <script>
            window.location.href = "{url}";
        </script>
    </head>
    <body>
    </body>
    </html>
    """)
