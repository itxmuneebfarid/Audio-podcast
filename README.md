
🎙️ PDF to Podcast Generator
Convert PDF documents into natural-sounding podcast episodes using FastAPI (backend) and Tailwind CSS (frontend). Ideal for learners, researchers, or anyone who prefers listening over reading.

🚀 Features
Upload any .pdf file

Extract and clean text

Generate realistic podcast-style audio using Edge TTS

Download the final .mp3 output

🧰 Requirements
Python 3.8+
fastapi
uvicorn
python-dotenv
pydub
edge-tts
langchain
langchain-community
FFmpeg (required by pydub for audio processing)
Download from: https://ffmpeg.org/download.html

Set FFmpeg paths in your Python code:
python
from pydub import AudioSegment, utils
AudioSegment.converter = r"D:\\ffmpeg\\bin\\ffmpeg.exe"
utils.get_prober_name = lambda: r"D:\\ffmpeg\\bin\\ffprobe.exe"
⚙️ Setup Instructions
1. Create and activate virtual environment
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
# Example requirements.txt:
fastapi
uvicorn
python-dotenv
pydub
edge-tts
langchain
langchain-community
▶️ Running the App
1. Start the FastAPI server
bash
uvicorn main:app --reload
Server runs at: http://127.0.0.1:8000

2. Launch the frontend
Open frontend/index.html in your browser (no server needed).

🧠 How It Works
PDF → Text Extraction → Cleaning → Dialogue Creation → TTS → Podcast (MP3)
LangChain: PDF parsing
📁 Project Structure
bash
Copy
Edit
📂 project-root/
├── main.py             # FastAPI backend
├── src/                # Processing and generation logic
├── util.py
├── .env
├── frontend/
│   └── index.html      # Tailwind-based UI
└── requirements.txt
🌟 Future Improvements
Multi-voice conversations

🙌 Credits
Backend: FastAPI

Voices: Microsoft Edge TTS

UI: Tailwind CSS

Audio: pydub + FFmpeg

Let me know if you’d li
