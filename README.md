# 🎙️ Offline Voice Assistant (Python + Local LLM)

## 📌 Overview

This project is a fully offline voice assistant built using Python. It combines a locally hosted Large Language Model (LLM) with an offline text-to-speech engine (Piper) to deliver a complete conversational experience — entirely on your machine.

The assistant allows you to type messages, receive intelligent AI-generated responses, and hear those responses spoken aloud in real time — all without needing an internet connection.

---

## ⚡ Core Features

* 🧠 **Offline AI Processing**
  Uses a locally installed LLM via Ollama (no cloud APIs)

* 🔊 **Natural Text-to-Speech**
  Powered by Piper voice for fast, realistic speech output

* 💬 **Continuous Conversation Loop**
  Input → AI Response → Speech → Repeat

* ⚡ **Live Streaming Responses**
  Responses appear in real-time as they are generated

* ✂️ **Smart Text Cleaning**
  Removes emojis, symbols, and formatting for smoother speech

* ⛔ **Interruptible Speech**
  Start typing anytime to stop current speech instantly

---

## 🧩 Tools & Technologies

This project integrates several powerful tools:

* **Python 3** – Core logic and execution
* **Ollama** – Runs the local LLM and handles response generation
* **Piper** – Offline text-to-speech engine
* **requests** – Communicates with the local LLM API
* **sounddevice** – Plays audio through your speakers
* **NumPy** – Handles audio data processing
* **threading** – Enables smooth, non-blocking speech
* **re (Regex)** – Cleans text for better speech output
* **json** – Handles streaming responses
* **os & sys** – System-level operations

All components are wired together in the main script .

---

# 🚀 FULL STEP-BY-STEP SETUP GUIDE

---

## 🪟 Windows Installation Guide

### ✅ Step 1: Install Python

1. Download Python from the official website
2. Run the installer
3. ⚠️ IMPORTANT: Check **"Add Python to PATH"**
4. Verify installation:

```bash
python --version
```

---

### ✅ Step 2: Install Required Python Packages

```bash
pip install requests sounddevice numpy
```

---

### ✅ Step 3: Install Ollama (Local LLM)

1. Download Ollama from its official website
2. Install and open it
3. Pull and run a model:

```bash
ollama run <your-model>
```

💡 Example:

```bash
ollama run llama3
```

---

### ✅ Step 4: Set Up Piper (Text-to-Speech)

1. Download a Piper voice model (e.g., `en_US-amy-medium`)
2. Place it in a known directory
3. Open the script and update this line:

```python
PIPER_MODEL_PATH = "path/to/your/voice/model.onnx"
```

---

### ✅ Step 5: Run the Assistant

```bash
python offline_voice_llm.py
```

---

## 🐧 Linux Installation Guide

### ✅ Step 1: Install Python & Pip

```bash
sudo apt update
sudo apt install python3 python3-pip
```

Verify:

```bash
python3 --version
```

---

### ✅ Step 2: Install Dependencies

```bash
pip3 install requests sounddevice numpy
```

---

### ✅ Step 3: Install Ollama

Follow official install instructions, then run:

```bash
ollama run <your-model>
```

---

### ✅ Step 4: Set Up Piper Voice

* Download a voice model
* Update the path in the script:

```python
PIPER_MODEL_PATH = "/home/user/path/to/model.onnx"
```

---

### ✅ Step 5: Run the Assistant

```bash
python3 offline_voice_llm.py
```

---

# ▶️ HOW TO USE THE ASSISTANT

### 🧪 Basic Usage Flow

```text
Start Program → Type Message → Get AI Response → Hear Voice → Repeat
```

### 🧾 Example Session

```bash
You: Hello
LLM: Hi there! How can I assist you today?
```

```bash
You: Explain what Python is
LLM: Python is a high-level programming language...
```

---

### ⛔ Exit Commands

To stop the assistant:

```bash
exit
```

or

```bash
quit
```

---

### ⚡ Pro Tips

* Start typing while it’s speaking to **interrupt audio instantly**
* Keep prompts clear for better responses
* Works completely offline once everything is installed

---

# 🔄 SYSTEM WORKFLOW

```text
User Input
   ↓
Local LLM (Ollama)
   ↓
Streaming Response (real-time text)
   ↓
Text Cleaning (remove noise)
   ↓
Piper TTS Conversion
   ↓
Audio Playback
   ↓
Loop continues...
```

---

# 🔒 100% OFFLINE GUARANTEE

* ❌ No internet required after setup
* 🔐 No data leaves your machine
* ⚡ Faster response time
* 🛡️ Full privacy and control

---

# 📂 PROJECT BEHAVIOR

* Runs continuously until stopped
* Handles multiple queries in one session
* Streams output in real time
* Speaks responses automatically
* Interrupts speech when new input is detected

---

# ✅ FINAL SUMMARY

This project gives you a **fully local AI assistant** that:

* Thinks using a local LLM
* Speaks using offline TTS
* Runs entirely on your machine
* Provides a fast, private, and interactive experience

---

🔥 If you're learning AI, automation, or building personal tools — this is a solid foundation project.

---


