from pydantic import BaseModel


class CourseRequest(BaseModel):
    
    title: str
    description: str
    author_id : int


class UpdateCourseRequest(BaseModel):

    id: int
    title: str
    description: str