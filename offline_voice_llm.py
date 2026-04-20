import requests
import json
import sounddevice as sd
import numpy as np
from piper import PiperVoice
import os
import sys
import re
import threading

# ================= CONFIG =================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "hadad/LFM2.5-1.2B:Q4_K_M"

PIPER_MODEL_PATH = os.path.expanduser(
    "~/Home Assistant/System Organs/Voices/Piper_voice/en_US-amy-medium.onnx"
)

# Personality prompt for the LLM
SYSTEM_PROMPT = (
    "You are a helpful, friendly, and concise assistant. "
    "Answer clearly and politely, like a real human assistant."
)

# ==========================================

print("Loading Piper voice into memory...")
try:
    voice = PiperVoice.load(PIPER_MODEL_PATH)
except Exception as e:
    print(f"Failed to load Piper model: {e}")
    sys.exit(1)

print("Piper loaded successfully.\n")

# Global variable to stop speech when user types
stop_speech_flag = False


# ================= SPEECH SANITIZATION =================

def clean_text_for_speech(text):
    """Sanitize LLM output for natural TTS playback."""
    # Remove emojis / non-ASCII symbols
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    # Remove markdown symbols
    text = re.sub(r'[*_~`#]', '', text)

    # Remove stage directions like (laughs) or [smiles]
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)

    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove standalone special characters
    text = re.sub(r'[<>^|{}]', '', text)

    # Replace multiple punctuation marks with single
    text = re.sub(r'([.!?]){2,}', r'\1', text)

    # Collapse extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# ================= SPEECH =================

def speak(text):
    """Speak text using Piper, interruptible if user types."""
    global stop_speech_flag
    stop_speech_flag = False

    try:
        for chunk in voice.synthesize(text):
            if stop_speech_flag:
                break
            audio_np = np.array(chunk.audio_float_array, dtype=np.float32)
            sd.play(audio_np, chunk.sample_rate, blocking=True)
    except Exception as e:
        print(f"\nSpeech error: {e}")


# ================= LLM STREAM =================

def ask_llm_stream(prompt):
    """
    Stream LLM response and speak after completion.
    Interrupts speech if user starts typing.
    """
    # Combine system personality + user prompt
    full_prompt = f"{SYSTEM_PROMPT}\nUser: {prompt}\nAssistant:"

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": full_prompt,
                "stream": True
            },
            stream=True,
            timeout=300
        )
    except requests.exceptions.RequestException as e:
        print(f"\nConnection error: {e}")
        return

    if response.status_code != 200:
        print(f"\nOllama error: {response.status_code}")
        return

    full_response = ""

    for line in response.iter_lines():
        if not line:
            continue

        try:
            data = json.loads(line.decode("utf-8"))
        except json.JSONDecodeError:
            continue

        token = data.get("response", "")
        done = data.get("done", False)

        print(token, end="", flush=True)
        full_response += token

        if done:
            print()
            break

    # Sanitize and speak in a separate thread
    cleaned = clean_text_for_speech(full_response)
    if cleaned:
        t = threading.Thread(target=speak, args=(cleaned,))
        t.start()


# ================= MAIN LOOP =================

def main():
    global stop_speech_flag

    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except KeyboardInterrupt:
            stop_speech_flag = True
            print("\nExiting...")
            break

        if user_input.lower() in ["exit", "quit"]:
            stop_speech_flag = True
            print("Goodbye.")
            break

        if not user_input:
            continue

        # Interrupt speech if user types a new prompt
        stop_speech_flag = True
        print("LLM:", end=" ", flush=True)
        ask_llm_stream(user_input)


# ==========================================

if __name__ == "__main__":
    main()

