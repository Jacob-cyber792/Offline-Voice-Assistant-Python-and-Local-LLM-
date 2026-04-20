# Offline-Voice-Assistant-Python-Local-LLM-
📌 Overview

This project is a fully offline voice assistant built using Python. It combines a locally hosted Large Language Model (LLM) with an offline text-to-speech engine to create a responsive, conversational assistant that runs entirely on your machine — no internet required.

The assistant takes user input, generates intelligent responses using a local AI model, and converts those responses into natural-sounding speech.

⚡ Core Features
🧠 Offline AI Brain
Uses a locally installed LLM to generate responses without cloud dependency
🔊 Text-to-Speech (TTS)
Powered by Piper voice for fast and natural offline speech synthesis
💬 Interactive Chat Loop
Continuous flow: input → response → speech → repeat
⚡ Streaming Responses
Displays responses in real-time as they are generated
✂️ Speech Cleanup System
Removes emojis, symbols, and formatting for smooth voice output
⛔ Interruptible Speech
Stops current speech instantly when new input is entered
🧩 Technologies & Tools Used

This project is built using the following tools and libraries:

Python 3 – Core programming language
Ollama (Local API) – Runs the offline LLM and handles text generation
Piper (TTS Engine) – Converts text into speech using local voice models
requests – Sends API requests to the local LLM server
sounddevice – Plays generated audio through the system speakers
NumPy – Processes audio data for playback
threading – Enables non-blocking speech playback
re (Regex) – Cleans and formats text for better speech output
json – Handles structured data from the LLM stream
os & sys – Manage file paths and system-level operations

All of these components work together inside the main script .

⚙️ How It Works (High-Level)
The user types a message into the terminal
The input is sent to a locally running LLM via Ollama
The LLM streams a response in real time
The response is cleaned for speech compatibility
Piper converts the text into audio
The assistant plays the audio output
The system loops and waits for the next input
🔒 Fully Offline Operation

This assistant runs 100% locally:

❌ No internet connection required
🔐 No data leaves your machine
⚡ Faster response times
🛡️ Full privacy and control

All processing — including AI reasoning and speech synthesis — happens on your device.

✅ Summary

A lightweight, privacy-focused voice assistant that:

Runs entirely offline
Combines AI intelligence with real-time speech
Uses powerful local tools for a seamless experience 
