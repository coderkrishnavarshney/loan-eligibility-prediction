from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .endpoints import predict, health
from src.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Loan Eligibility Prediction API",
    description="API for predicting loan eligibility using ML models",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(predict.router, prefix="/api/v1", tags=["prediction"])
app.include_router(health.router, prefix="/api/v1", tags=["health"])

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Loan Prediction API")