PDF to Podcast Generator:

Convert your PDF documents into engaging, natural-sounding podcast episodes using FastAPI (backend) and Tailwind CSS (frontend). This tool transforms static reading material into audio content, ideal for learners, researchers, or anyone who prefers to listen rather than read.

Project Overview
This project allows users to:

Upload any .pdf file.

Automatically extract and clean its contents.

Generate a podcast-style dialogue from the content.

Convert the dialogue into an .mp3 file using realistic AI voices.

Download the final podcast directly through a web interface.
Requirements
Install dependencies via pip:
pip install fastapi uvicorn python-dotenv pydub edge-tts
Also download and configure FFmpeg:
python
Copy
Edit

# In your Python code, set paths like this:
AudioSegment.converter = r"D:\\ffmpeg\\bin\\ffmpeg.exe"
pydub.utils.get_prober_name = lambda: r"D:\\ffmpeg\\bin\\ffprobe.exe"
FFmpeg is required by pydub for audio processing and must be downloaded separately.
Setting Up Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
# Activate it:
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Then install:
pip install -r requirements.txt
Example requirements.txt:

nginx
Copy
Edit
fastapi
uvicorn
python-dotenv
pydub
edge-tts
How to Run the App
1. Start FastAPI Backend
bash
Copy
Edit
uvicorn main:app --reload
This runs the server at http://127.0.0.1:8000.

2. Open Frontend Website
Use the HTML file provided (index.html). You can open it directly in a browser, or serve it using Python or any web server.

Frontend Overview
A clean, minimal UI built with Tailwind CSS, providing:

PDF upload functionality

Status updates

Podcast download button (once generated)

Preview
<!-- Replace with real screenshot if available -->

📁 Frontend File Structure
plaintext
Copy
Edit

📂 project-root

├── main.py  # FastAPI backend
├── src/          # Text processing and podcast logic
├── util.py

├── .env

├── frontend/

│   └── index.html  # Tailwind-based UI
└── requirements.txt

How It Works
scss
Copy
Edit
PDF →Text Extraction → Cleaning → Dialogue Generation → TTS (Edge TTS)→ MP3 Podcast Text Extraction:
Using LangChain loader

Text Cleaning: Removes unwanted headers/footers

Podcast Logic: Transforms content into conversational style

Text-to-Speech: Edge TTS with voice customization

Audio Output: Combined into final_podcast.mp3

Future Enhancements
Multiple speaker voices and styles

Language translation support

Deployment to cloud (Render, HuggingFace, etc.)

 Mobile-friendly UI

Podcast series feature for long PDFs

Analytics dashboard (time saved, word count, etc.)

Credits:
Built using FastAPI

Voices generated with Edge TTS

UI styled using Tailwind CSS

Audio managed by pydub

