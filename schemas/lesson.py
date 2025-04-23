from pydantic import BaseModel


class LessonRequest(BaseModel):

    course_id: int
    title: str
    video_url: str
    content: str