"""
CareerForge - ElevenLabs Voice Integration
==========================================
Two agents:
  1. System Assistant (Hope - bubbly female voice)
  2. InterviewAI (Elon Musk - cloned voice)
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="CareerForge Voice API")

api_key = os.getenv("ELEVENLABS_API_KEY")
agent_id = os.getenv("ELEVENLABS_AGENT_ID")  # Hope - system assistant
interview_agent_id = os.getenv("ELEVENLABS_INTERVIEW_AGENT_ID")  # Elon - interviewer

client = ElevenLabs(api_key=api_key)

# Voice IDs (from .env)
HOPE_VOICE_ID = os.getenv("HOPE_VOICE_ID")
INTERVIEW_VOICE_ID = os.getenv("INTERVIEW_VOICE_ID")


class SpeakRequest(BaseModel):
    text: str
    voice: str = "hope"  # "hope" or "elon"


# ─── Web UI ────────────────────────────────────────────────

@app.get("/")
async def root():
    """Serve the voice chat web UI."""
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())


# ─── Agent Config Endpoints ────────────────────────────────

@app.get("/api/config")
async def get_config():
    """Return both agent configs for the frontend."""
    return {
        "assistant_agent_id": agent_id,
        "interview_agent_id": interview_agent_id,
    }


@app.get("/api/signed-url")
async def get_signed_url(mode: str = "assistant"):
    """Get a signed URL for ElevenLabs Conversational AI WebSocket.
    
    Query param: mode=assistant (default) or mode=interview
    """
    target_agent = interview_agent_id if mode == "interview" else agent_id

    if not target_agent:
        raise HTTPException(
            status_code=500,
            detail=f"Agent ID for '{mode}' not configured in .env"
        )
    try:
        response = client.conversational_ai.get_signed_url(agent_id=target_agent)
        return {"signed_url": response.signed_url, "mode": mode}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─── One-Shot TTS ──────────────────────────────────────────

@app.post("/speak")
async def speak(request: SpeakRequest):
    """One-shot text-to-speech with voice selection."""
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required")

    voice_id = INTERVIEW_VOICE_ID if request.voice == "interview" else HOPE_VOICE_ID

    try:
        audio_generator = client.text_to_speech.convert(
            text=request.text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        def iterfile():
            for chunk in audio_generator:
                yield chunk

        return StreamingResponse(iterfile(), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ─── Health ────────────────────────────────────────────────

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "assistant_agent": agent_id is not None,
        "interview_agent": interview_agent_id is not None,
        "api_key": api_key is not None,
    }
