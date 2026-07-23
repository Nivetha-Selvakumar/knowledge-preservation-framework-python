from pydantic import BaseModel


class GithubResponse(BaseModel):
    status: str
    message: str
