# MultiModal

## Experimented with 2 approaches

1) MultiModalSearch 

Video -> Image Frame ->  Clip Embedding (multi-modal) <- Text Search 

Video -> Whisper -> Transcript -> Text Embedding <- Text Search

3) Video Segment

Video -> Video Segment -> VLM -> Generates Transcript, Scene description -> Text Embedding <- Text Search
