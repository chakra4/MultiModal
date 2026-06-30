# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Project Overview
Video Q&A system using Google Gemini Pro Vision, ChromaDB, and OpenCV for video analysis and question answering.

## Code Mode Notes
- Python 3.12.9 with `uv` package manager
- Jupyter notebook-based workflow in `video_qa_system.ipynb`
- ChromaDB uses default all-MiniLM-L6-v2 embeddings (not true multi2vec yet)
- Video segmentation creates `video_segments_<video_name>/` directories at runtime
- Gemini API uploads video files for analysis (not frame-by-frame)
- Gemini API calls are sequential to avoid rate limits and allow file processing
- No access to MCP and Browser tools in this mode