# AI Text Summary App

A Flask-based backend API that uses OpenAI GPT-3.5 to summarize transcripts and extract action items.

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment variables:**
   The `.env` file is already configured with your OpenAI API key.

4. **Run the application:**
   ```bash
   python app.py
   ```

   The server will start on `http://localhost:5000`

**Note:** Always activate the virtual environment before running the application:
```bash
source venv/bin/activate
```

## API Usage

### POST /summarize

Send a transcript to get a summary and action items.

**Request:**
```json
{
  "transcript": "Your meeting transcript text here..."
}
```

**Response:**
```json
{
  "summary": "• Meeting summary in bullet points\n• Key action items\n• Important decisions"
}
```

**Error Response:**
```json
{
  "error": "Error message"
}
```

## Testing

You can test the API using curl:

```bash
curl -X POST http://localhost:5000/summarize \
  -H "Content-Type: application/json" \
  -d '{"transcript": "Today we discussed the quarterly budget. John will prepare the financial report by Friday. Sarah will coordinate with the marketing team."}'
```

## Next Steps

- Add frontend UI for file upload
- Implement text chunking for large documents
- Add audio transcription with Whisper API 