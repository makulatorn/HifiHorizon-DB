from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .routers import products
import uvicorn
import os
from app.models.base import Base
from app.database import engine
import app.models.product
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

print("=== FORCING TABLE CREATION ON APP START ===")
Base.metadata.create_all(bind=engine)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Development
        "https://hifihorizon-db.onrender.com"  # Production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
class CORSMiddlewareForStatic(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if request.url.path.startswith("/static/"):
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "*"
        return response

app.add_middleware(CORSMiddlewareForStatic)

# Mount static files
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "..", "static")),
    name="static"
)
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
            <h1>HiFi Horizon API</h1>
            <p>Visit <a href="/docs">documentation</a> for API endpoints.</p>
            <p>Browse our <a href="/products">products</a>.</p>
        </body>
    </html>
    """
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)