from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .routers import products

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    #Url allowed to access the API
    allow_origins=["http://localhost:5173"],  #React URL
    #When true allows cookies and authtication headers
    allow_credentials=True,
    #Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    #Allows all headers (Content-Type, Authorization, etc.)
    allow_headers=[
        "Content-Type", #Needed for JSON requests
        "Authorization", #Required for token-based auth
        "Access-Control-Allow-Headers", #CORS speification
        "Origin", #Browser sends origin header
        "Accept" #Specifies acceptable response format
    ]
)

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