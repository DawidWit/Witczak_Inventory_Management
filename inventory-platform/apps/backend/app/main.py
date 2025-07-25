from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routes import auth, items, users
from app.core.config import settings

app = FastAPI(title="Inventory Backend API", version="1.0.0")

app.include_router(items.router)
app.include_router(users.router)
app.include_router(auth.router)

# CORS setup (customize as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok"}
