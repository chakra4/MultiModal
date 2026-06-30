# Multimodal Video RAG System

A comprehensive system for downloading YouTube videos and performing multimodal question-answering using Retrieval-Augmented Generation (RAG).

## Features

1. **YouTube Video Downloader** - Download videos from YouTube
2. **Multimodal RAG System** - Question-answering from video content using:
   - Frame extraction and visual search (CLIP embeddings)
   - Audio transcription (Whisper)
   - Semantic search over transcripts
   - Vector database storage (ChromaDB)

## Target Video
- URL: https://www.youtube.com/watch?v=84id2dzpwU0

## Installation

The project uses UV for dependency management with Python 3.12.9.

The virtual environment and dependencies are already set up:
```bash
# Virtual environment created at: .venv
# yt-dlp==2026.6.9 installed
```

If you need to recreate the environment:
```bash
uv init --python 3.12.9
uv add yt-dlp
```

## Usage

Run the script using UV:
```bash
uv run python download_youtube_video.py
```

Or activate the virtual environment and run:
```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows

python download_youtube_video.py
```

## Features

- Downloads the best quality video available in MP4 format
- Automatically merges video and audio streams
- Creates a `downloads` directory for output files
- Displays video information before downloading (title, duration, uploader)
- Error handling and user-friendly messages

## Output

The downloaded video will be saved in the `./downloads/` directory with the video's title as the filename.

## Multimodal RAG Notebook

The [`multimodal_video_rag.ipynb`](multimodal_video_rag.ipynb:1) notebook provides:

### Capabilities
- **Frame Extraction**: Extracts frames from videos at regular intervals
- **Audio Transcription**: Uses Whisper AI to transcribe video audio
- **Multimodal Embeddings**:
  - Text embeddings using Sentence Transformers
  - Image embeddings using CLIP
- **Vector Database**: ChromaDB for efficient similarity search
- **Question Answering**: Ask questions about video content and get relevant:
  - Transcript segments with timestamps
  - Video frames with visual context

### Usage

1. First, download a video:
```bash
uv run python download_youtube_video.py
```

2. Open and run the Jupyter notebook:
```bash
uv run jupyter notebook multimodal_video_rag.ipynb
```

3. The notebook will:
   - Process all videos in `./downloads/`
   - Extract frames and transcribe audio
   - Index content in ChromaDB
   - Enable question-answering

### Example Queries
- "What is the main topic discussed in the video?"
- "Show me scenes with people talking"
- "What are the key points mentioned?"
- "Summarize what was said about [topic]"

## Requirements

- Python 3.12.9 (managed by UV)
- All dependencies installed via `uv add`

## Project Structure

```
.
├── download_youtube_video.py    # YouTube downloader script
├── multimodal_video_rag.ipynb   # Multimodal RAG notebook
├── downloads/                    # Downloaded videos
├── video_processing_output/      # Extracted frames and transcripts
│   ├── frames/
│   ├── audio/
│   └── transcripts/
└── chroma_db/                    # Vector database storage
```

## Notes

- The system uses `yt-dlp` for video downloads
- Whisper model (base) is used for transcription
- CLIP model is used for visual understanding
- All embeddings are stored in ChromaDB for fast retrieval
- Make sure you have sufficient disk space for videos and processing
- Respect YouTube's Terms of Service when downloading videos