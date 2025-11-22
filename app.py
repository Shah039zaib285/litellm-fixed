from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import litellm
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(title="Mega Agency AI Server", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Mega Agency AI Server",
        "timestamp": "2024-01-01T00:00:00Z"  # This would be dynamic in real implementation
    }

# AI chat completion endpoint
@app.post("/v1/chat/completions")
async def chat_completion(request: dict):
    try:
        logger.info(f"AI request received: {request}")
        
        # Your LiteLLM configuration here
        # This is a simplified version
        response = {
            "choices": [
                {
                    "message": {
                        "content": "This is a sample AI response. Configure LiteLLM with your actual AI providers.",
                        "role": "assistant"
                    }
                }
            ]
        }
        
        return response
        
    except Exception as e:
        logger.error(f"AI service error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Mega Agency AI Server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)