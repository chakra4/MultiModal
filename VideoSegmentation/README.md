# Video Q&A System

A Python-based system for extracting insights from videos using Google Gemini Pro Vision, generating embeddings, and storing them in ChromaDB for question answering.

## Features

- **Video Segmentation**: Split long videos into shorter video clips at configurable durations
- **AI-Powered Analysis**: Use Google Gemini Pro Vision to analyze and describe video segments
- **Semantic Search**: Store frame descriptions in ChromaDB with embeddings
- **Question Answering**: Query videos using natural language questions
- **Interactive Notebook**: Jupyter notebook interface for easy experimentation

## Prerequisites

- Python 3.12.9
- [uv](https://github.com/astral-sh/uv) package manager
- Google API Key for Gemini Pro Vision

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd VideoSegmentation
   ```

2. **Create virtual environment with uv**:
   ```bash
   uv venv --python 3.12.9
   ```

3. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

5. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## Usage

### Running the Jupyter Notebook

1. **Activate the virtual environment** (if not already activated):
   ```bash
   source .venv/bin/activate
   ```

2. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

3. **Open `video_qa_system.ipynb`** in your browser

4. **Update the video path** in the notebook:
   ```python
   VIDEO_PATH = "path/to/your/video.mp4"
   ```

5. **Run the cells** to:
   - Split video into shorter segments
   - Analyze video segments with Gemini Pro Vision
   - Store segment descriptions in ChromaDB
   - Query the video with natural language questions

### Example Workflow

```python
# 1. Segment video into 30-second clips
segmenter = VideoSegmenter("my_video.mp4")
segments_info = segmenter.segment_video(segment_duration=30.0)

# 2. Analyze segments with Gemini
analyzer = GeminiAnalyzer()
segments_info = analyzer.analyze_segments_batch(segments_info)

# 3. Store in ChromaDB
db = VideoChromaDB(collection_name="my_videos")
db.add_segments(segments_info, "my_video")

# 4. Query the video
results = db.query("What activities are happening?", n_results=3)
```

## Project Structure

```
VideoSegmentation/
├── .venv/                      # Virtual environment (created by uv)
├── src/                        # Source package
│   └── __init__.py
├── video_segments/             # Segmented video clips (created at runtime)
├── chroma_db/                  # ChromaDB storage (created at runtime)
├── video_qa_system.ipynb       # Main Jupyter notebook
├── pyproject.toml              # Project dependencies
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore patterns
├── README.md                   # This file
└── AGENTS.md                   # AI assistant guidelines

```

## Key Components

### VideoSegmenter
Splits long videos into shorter video clips of specified duration using OpenCV.

### GeminiAnalyzer
Uses Google Gemini Pro Vision to analyze and describe video segments in detail. Uploads video segments to Gemini API for comprehensive analysis.

### VideoChromaDB
Manages ChromaDB collection for storing and querying video segments with semantic search.

## Configuration

### Video Segment Duration
Adjust the `SEGMENT_DURATION` variable in the notebook to control the length of each video segment:
- `30.0` = 30-second segments
- `60.0` = 1-minute segments
- `15.0` = 15-second segments

### Query Results
Modify `n_results` parameter in queries to control how many relevant segments are returned.

## Dependencies

Main dependencies (see `pyproject.toml` for complete list):
- `google-generativeai` - Google Gemini API
- `chromadb` - Vector database for embeddings
- `opencv-python` - Video processing
- `pillow` - Image handling
- `jupyter` - Interactive notebook environment
- `python-dotenv` - Environment variable management

## Troubleshooting

### API Key Issues
- Ensure your `.env` file contains a valid `GOOGLE_API_KEY`
- Check that the API key has access to Gemini Pro Vision

### Video Format Issues
- Supported formats: MP4, AVI, MOV, MKV
- If you encounter codec issues, try converting your video to MP4 with H.264 encoding

### Memory Issues
- For long videos, increase the `SEGMENT_DURATION` to create fewer segments
- Gemini API has file size limits; keep segments under 2GB

## Notes

- The notebook uses ChromaDB's default embedding function (all-MiniLM-L6-v2) for text embeddings
- For true multi2vec embeddings, you would need to implement a custom embedding function
- Video segmentation creates a `video_segments_<video_name>` directory for each video
- ChromaDB data is persisted in the `chroma_db` directory
- Gemini API uploads and processes video files; processing time depends on video length

## License

This project is provided as-is for educational and research purposes.

## Contributing

Feel free to submit issues and enhancement requests!