from pydantic import BaseModel

"""
Base class for calling end-poinnt - /remember
"""


class RememberModel(BaseModel):
    video_id: str


"""
Base class for youtube transcript
"""


class YoutubeTransScriptModel(BaseModel):
    text: str
    start: float
    duration: float

class Query(BaseModel):
    query: str
