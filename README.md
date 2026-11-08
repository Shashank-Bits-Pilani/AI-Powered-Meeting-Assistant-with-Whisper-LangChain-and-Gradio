# AI-Powered Meeting Assistant

An AI-powered application that converts meeting audio into text, improves transcription quality, and generates structured meeting summaries and action items.

## Features

- **Speech-to-Text:** Transcribes English meeting audio using OpenAI Whisper.
- **Transcript Correction:** Uses Llama 3.2 to correct transcription errors.
- **Meeting Summarization:** Generates structured meeting minutes using LangChain and Ollama.
- **Action Item Extraction:** Identifies tasks, responsibilities, and deadlines.
- **File Download:** Exports meeting minutes as a text file.
- **Web Interface:** Provides an interactive interface using Gradio.

## Technology Stack

- Python
- Hugging Face Transformers
- OpenAI Whisper
- Ollama (Llama 3.2)
- LangChain
- Gradio
- PyTorch

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Powered-Meeting-Assistant.git
cd AI-Powered-Meeting-Assistant
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment and install dependencies:

```bash
python -m pip install -r requirements.txt
```

### 3. Install Ollama

Download Ollama from https://ollama.com and install it.

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 4. Install FFmpeg

Install FFmpeg and make sure it is available on your system PATH.

### 5. Run the application

```bash
python speech_analyzer.py
```

Open the local Gradio URL shown in your terminal.

## How It Works

1. Upload an English meeting audio recording.
2. Whisper converts the audio into text.
3. Llama 3.2 corrects transcription errors.
4. LangChain and Llama generate meeting minutes and action items.
5. Download the results as a text file.

## Future Enhancements

- Speaker diarization
- Multilingual transcription
- Meeting transcript search using RAG
- PDF export
- Improved processing speed

## Privacy

The application uses local Ollama inference for language-model processing. Review the privacy behavior of all configured components before processing confidential recordings.
