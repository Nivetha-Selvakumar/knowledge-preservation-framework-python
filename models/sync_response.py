from pydantic import BaseModel


class SyncResponse(BaseModel):
    status: str
    repositories_processed: int
    knowledge_files: list
