# from pydantic import BaseModel


# class GithubSyncRequest(BaseModel):
#     token: str


from pydantic import BaseModel


class GithubSyncRequest(BaseModel):
    repositoryId: str
    repositoryName: str
    owner: str
    token: str
