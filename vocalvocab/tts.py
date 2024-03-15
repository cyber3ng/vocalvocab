from pathlib import Path
from openai import OpenAI
import hashlib
from tempfile import gettempdir


def generate_speech(text):
    client = OpenAI()

    # Save audio files to the temp directory
    resources_dir = Path(gettempdir()) / "nativespeak_audio"
    resources_dir.mkdir(parents=True, exist_ok=True)

    # filename is md5 hash of the phrase for bookkeeping
    filename = hashlib.md5(text.encode('utf-8')).hexdigest() + ".mp3"
    speech_file_path = resources_dir / filename

    # Generate the speech using OpenAI's API
    response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=text
    )

    # Stream the response to the file
    response.stream_to_file(str(speech_file_path))
    return str(speech_file_path)
