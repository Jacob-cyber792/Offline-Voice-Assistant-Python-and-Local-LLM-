# Offline Voice Assistant (Python + Local LLM)
📌 Overview

This project is a fully offline voice assistant built with Python. It uses a locally hosted Large Language Model (LLM) and an offline text-to-speech engine to generate and speak responses — all without requiring an internet connection.

⚡ Features
🧠 Offline AI Responses using a local LLM
🔊 Text-to-Speech with Piper voice
💬 Continuous Chat Loop (input → response → speech)
⚡ Real-Time Streaming Output
✂️ Clean Speech Processing for natural playback
⛔ Interruptible Speech when new input is entered
🧩 Tools & Technologies
Python 3
Ollama (Local LLM API)
Piper (TTS Engine)
requests – API communication
sounddevice + NumPy – Audio playback
threading – Non-blocking speech
re, json, os, sys – Data handling & processing

(All integrated in the main script )

⚙️ How It Works
User enters text input
Input is sent to the local LLM
Response is streamed and displayed
Text is cleaned and converted to speech
Audio is played, then the loop repeats
🔒 Offline Capability
No internet required
No external data sharing
Fast and private execution
✅ Summary

A simple, fast, and privacy-focused voice assistant that runs entirely on your local machine.
