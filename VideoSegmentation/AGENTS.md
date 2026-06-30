# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project Overview
Video Q&A system using Google Gemini Pro Vision, ChromaDB, and OpenCV for video analysis and question answering.

## Environment Setup
- Python 3.12.9 managed with `uv` package manager
- Virtual environment: `.venv` (activate with `source .venv/bin/activate`)
- Dependencies installed via: `uv pip install -e .`
- Requires `GOOGLE_API_KEY` in `.env` file for Gemini API access

## Key Commands
```bash
# Setup
uv venv --python 3.12.9
source .venv/bin/activate
uv pip install -e .

# Run Jupyter
jupyter notebook
```

## Project Structure
- `video_qa_system.ipynb` - Main notebook with complete pipeline
- `src/` - Python package (minimal, used for editable install)
- `video_segments/` - Runtime directory for segmented video clips
- `chroma_db/` - ChromaDB persistent storage
- `.env` - API keys (not in git)

## Non-Obvious Patterns
- ChromaDB uses default all-MiniLM-L6-v2 embeddings (not true multi2vec yet)
- Video segmentation creates separate directories per video: `video_segments_<video_name>/`
- Gemini API uploads video files for analysis (not frame-by-frame)
- Video segments stored as MP4 files with time range in filename
- Gemini API calls are sequential to avoid rate limits and allow file processing
- ChromaDB collection persists between runs in `./chroma_db` directory