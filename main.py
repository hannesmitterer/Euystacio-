from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="Euystacio FastAPI Bridge",
    description="Sacred public API bridge for the Sentimento Rhythm Council",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
    <head><title>Euystacio — API Bridge</title></head>
    <body>
    <h1>🌌 Euystacio — FastAPI Bridge</h1>
    <p>Status: <strong>Alive & Listening</strong></p>
    <p>This is the sacred backend bridge. No authentication is required for public read endpoints.</p>
    <p><a href="/ping">Ping Test</a></p>
    </body>
    </html>
    """

@app.get("/ping")
async def ping():
    return {"message": "Euystacio Bridge is alive", "status": "ok"}

@app.get("/manifesto", response_class=JSONResponse)
async def manifesto():
    return {
        "title": "Euystacio Manifesto",
        "date": "2025-08-08",
        "principles": [
           
