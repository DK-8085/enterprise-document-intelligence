from fastapi import FastAPI

app= FastAPI(
    title="enterprise document intelligence",
    description="An AI-powered document intelligence platform",
    version="0.1.0",
    )

@app.get("/health")
async def health_check():
    return{
        "status": "healthy",
        "service": "document-intelligence",
        "version": "0.1.0",
        }

@app.get("/")
async def root():
    return {
        "message": "Enterprise Document Intelligence API"
    }
