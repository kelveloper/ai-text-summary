from flask import Flask, request, jsonify, send_from_directory
import openai
import os
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable requests from frontend

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    transcript = data.get('transcript', '')

    if not transcript:
        return jsonify({'error': 'No transcript provided'}), 400

    prompt = f"""
    You are an empathetic meeting assistant who understands both content and context. 
    
    Please analyze this transcript with human-centered thinking:
    
    1. **Meeting Purpose & Tone**: What was the main intention? (decision-making, brainstorming, problem-solving, update sharing)
    2. **Key Insights**: What are the most important takeaways that someone would want to remember weeks later?
    3. **Action Items**: List specific, actionable next steps with context about why they matter
    4. **Follow-up Questions**: What important topics were mentioned but not fully resolved?
    5. **Emotional Undertones**: Were there any concerns, excitement, or tensions worth noting?
    
    Format your response clearly with these sections. Be specific and helpful, not just factual.
    
    Transcript:
    {transcript}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )

        output = response['choices'][0]['message']['content']
        return jsonify({'summary': output})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 