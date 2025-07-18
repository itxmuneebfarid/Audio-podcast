
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
import os
from typing import List
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

class PodcastDialogue(BaseModel):
    speaker1: List[str] = Field(description="Dialogues of speaker 1")
    speaker2: List[str] = Field(description="Dialogues of speaker 2")
def make_podcast_dialogue(cleaned_text):

        llm_structured = llm.with_structured_output(PodcastDialogue)
        response = llm_structured.invoke(
        f"Convert the following cleaned text into a podcast dialogue "
        f"between two speakers, as JSON with speaker1 and speaker2.\n\n"
        f"Both Speakers should have equal number of dialogues."
        f"{cleaned_text}"
    )
        podcast = response.model_dump()

        with open("podcast.txt", "w", newline="\n") as f:
            for key, lines in podcast.items():
                 f.write(key)
                 f.write("\n---------------\n")
                 for line in lines:
                      f.write(line)
                      f.write("\n")
                 f.write("\n---------------\n")

        return podcast