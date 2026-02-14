# ElevenLabs FastAPI Integration

## Setup

1. **Add your API Key**:
   Open `.env` and replace `YOUR_API_KEY` with your actual ElevenLabs API key.

   ```
   ELEVENLABS_API_KEY=sk_...
   ```

2. **Run the Server**:
   You can use the helper script:

   ```bash
   ./run.sh
   ```

   Or manually:

   ```bash
   source venv/bin/activate
   uvicorn main:app --reload
   ```

## Usage

**Endpoint**: `POST /speak`

**Request Body**:

```json
{
  "text": "Hello, this is a test."
}
```

**Example (Curl)**:

```bash
curl -X POST "http://localhost:8000/speak" \
     -H "Content-Type: application/json" \
     -d '{"text": "Refactoring works!"}' \
     --output response.mp3
```

## Configuration

The app is configured to use:

- **Model**: `eleven_multilingual_v2`
- **Voice ID**: `JBFqnCBsd6RMkjVDRZzb`
