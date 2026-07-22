from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.base import Base
from database.database import engine

import models.user
import models.document
import models.chat
import models.analytics

from api.routes.upload import router as upload_router
from api.routes.chat import router as chat_router
from api.routes.document import router as document_router
from api.routes.search import router as search_router
from api.routes.analytics import router as analytics_router


Base.metadata.create_all(bind=engine)


app = FastAPI(

    title="IndustrialBrain AI",

    version="1.0.0",

    description="AI-powered Industrial Document Intelligence Platform"

)


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


app.include_router(

    upload_router,

    prefix="/api",

    tags=["Upload"]

)

app.include_router(

    chat_router,

    prefix="/api",

    tags=["Chat"]

)

app.include_router(

    document_router,

    prefix="/api",

    tags=["Documents"]

)

app.include_router(

    search_router,

    prefix="/api",

    tags=["Search"]

)

app.include_router(

    analytics_router,

    prefix="/api",

    tags=["Analytics"]

)


@app.get("/")
def home():

    return {

        "status": "running",

        "application": "IndustrialBrain AI",

        "version": "1.0.0",

        "message": "IndustrialBrain AI Backend Running"

    }


@app.get("/health")
def health():

    return {

        "status": "healthy",

        "database": "connected",

        "api": "online"

    }