from pydub import AudioSegment
import edge_tts
import os
async def text_to_speech(text, voice, filename):
    tts = edge_tts.Communicate(text, voice)
    await tts.save(filename)

async def create_podcast_audio(podcast_data):
    combined = AudioSegment.silent(duration=0)
    counter = 1

    os.makedirs("temp", exist_ok=True)
    for s1, s2 in podcast_data:
        file1 = f"temp/speech_{counter}_1.mp3"
        file2 = f"temp/speech_{counter}_2.mp3"

        VOICE_1 = "en-US-JennyNeural"  # female
        VOICE_2 = "en-US-GuyNeural"    # male

        await text_to_speech(s1, VOICE_1, file1)
        await text_to_speech(s2, VOICE_2, file2)

        audio1 = AudioSegment.from_file(file1)
        audio2 = AudioSegment.from_file(file2)

        combined += audio1 + audio2
        counter += 1

    combined.export("final_podcast.mp3", format="mp3")
    print("✅ Podcast audio created as final_podcast.mp3")
