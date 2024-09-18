from youtube_transcript_api import YouTubeTranscriptApi
from model.models import YoutubeTransScriptModel

"""
This function fetches all the transcripts from the given video ID

Args:
    video_id: ID of the video from which we want to fetch the transcript
"""
def fetch_transcipt(video_id: str):
    transcripts = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_object_list = []
    for transcript in transcripts:
        transcript_object = YoutubeTransScriptModel(**transcript)
        transcript_object_list.append(transcript_object)
    return transcript_object_list