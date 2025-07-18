import edge_tts
async def text_to_speech(text, voice, filename):
    tts = edge_tts.Communicate(text, voice)
    await tts.save(filename)