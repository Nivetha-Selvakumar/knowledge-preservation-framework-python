from pydantic import BaseModel


class GithubRequest(BaseModel):
    userId: str
    githubToken: str
