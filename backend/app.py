
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from analysis import analyze_bio
from rewrite import rewrite_bio_with_gemini


app = FastAPI(
    title="AI Green / Red Flag Detector",
    description="Analyze dating bios for green, yellow, and red flags and suggest improvements.",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class BioRequest(BaseModel):
    bio: str

class RewriteRequest(BaseModel):
    bio: str
    tone: str = "confident"



@app.post("/classify")
def classify_bio(request: BioRequest):
    """
    Analyze a dating bio and return flags, scores, and explanations.
    """
    return analyze_bio(request.bio)

@app.post("/rewrite")
def rewrite_bio(request: RewriteRequest):
    """
    Analyze a dating bio and return an improved rewritten version.
    """
    analysis = analyze_bio(request.bio)
    improved_bio = rewrite_bio_with_gemini(
        request.bio,
        analysis,
        target_tone=request.tone
    )

    return {
        "analysis": analysis,
        "improved_bio": improved_bio
    }
