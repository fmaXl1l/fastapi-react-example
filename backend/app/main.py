from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import items, users

app = FastAPI(
    title="FastAPI React Example",
    description="A sample project with FastAPI backend and React frontend",
    version="0.1.0"
)

# Configure CORS
origins = [
    "http://localhost:3000",  # React frontend
    "http://localhost:5173",  # Vite frontend (if using Vite)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(items.router, prefix="/api")
app.include_router(users.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI React Example API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
