from pydantic import BaseModel
from uuid import UUID

class WorkspaceIn(BaseModel):
    name: str
    description: str


class WorkspaceOut(BaseModel):
    id: UUID
    name: str
    description: str


class DocumentIn(BaseModel):
    name: str
    description: str
    workspace_id: UUID

class DocumentOut(BaseModel):
    id: UUID
    name: str
    description: str
    workspace_id: UUID