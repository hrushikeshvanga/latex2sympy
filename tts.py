"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
from google.cloud.texttospeech_v1.types import SynthesizeSpeechResponse

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account_key.json"


def generate_mp3(words: str) -> bytes:
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    print(f'  -> Text to speech: reading {words}')
    synthesis_input = texttospeech.SynthesisInput(text=words)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Neural2-D"
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    print(f'  -> Text to speech: done')
    # The response's audio_content is binary.
    return response.audio_content

    # filename = "output.mp3"
    # with open(filename, "wb") as out:
    #     # Write the response to the output file.
    #     out.write(response.audio_content)
    #     print('Audio content written to file', filename)
