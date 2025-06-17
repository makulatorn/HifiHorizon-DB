from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .routers import products

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(products.router)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>HiFi Horizon</title>
        </head>
        <body>
            <h1>Welcome to HiFi Horizon</h1>
            <p>Visit <a href="/docs">documentation</a> for API endpoints.</p>
            <p>Browse our <a href="/products">products</a>.</p>
        </body>
    </html>
    """