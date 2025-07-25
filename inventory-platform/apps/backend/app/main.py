from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.database import engine
from app.models import user, resource
from app.core.config import settings

# Create database tables
user.Base.metadata.create_all(bind=engine)
resource.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME, 
    description=settings.DESCRIPTION, 
    version=settings.VERSION, 
    docs_url=settings.DOCS_URL, 
    redoc_url=settings.REDOC_URL 
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return {"message": f"{settings.PROJECT_NAME} API", "version": settings.VERSION}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
