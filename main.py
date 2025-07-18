from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

import tempfile
import shutil
import os

from util import load_pdf_text
from src.cleaned_pdf import clean_document_text
from src.podcast_ import make_podcast_dialogue
from src.refactor_podcast import refactor_podcast
from src.create_podcast import create_podcast_audio

from pydub import AudioSegment
AudioSegment.converter = r"D:\ffmpeg-2025-07-10-git-82aeee3c19-full_build\bin\ffmpeg.exe"
import pydub
pydub.utils.get_prober_name = lambda: r"D:\ffmpeg-2025-07-10-git-82aeee3c19-full_build\bin\ffprobe.exe"

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev: allow all. In production, set your frontend domain here.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-podcast/")
async def generate_podcast(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    try:
        if os.path.exists("final_podcast.mp3"):
            os.remove("final_podcast.mp3")
        # Save uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name
            print(f"✅ Upload received: {file.filename}")
            print(f"🧪 Saved PDF to: {tmp_path}")

        # Process and clean
        docs = load_pdf_text(tmp_path)
        raw_text = "\n".join(doc.page_content for doc in docs)
        cleaned_text = clean_document_text(raw_text)
        podcast_json = make_podcast_dialogue(cleaned_text)
        refactored_podcast = refactor_podcast(podcast_json)

        # Run heavy TTS in background
        background_tasks.add_task(create_podcast_audio, refactored_podcast)
        background_tasks.add_task(shutil.rmtree, "temp")

        return JSONResponse({"status": "processing"}, background=background_tasks)

    except Exception as e:
        print("❌ Error:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/download", response_class=FileResponse)
def download_podcast():
    try:
        file_path = "final_podcast.mp3"
        if os.path.exists(file_path):
            return FileResponse(
                path=file_path,
                media_type="audio/mpeg",
                filename="podcast.mp3"
            )
        else:
            return JSONResponse(content={"error": "Podcast file not ready yet."}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
