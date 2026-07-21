from fastapi import HTTPException
from uuid import UUID

from app.storage import workspaces


def get_workspace_by_id(workspace_id: UUID):
    for workspace in workspaces:
        if workspace.id == workspace_id:
            return workspace

    raise HTTPException(
        status_code=404,
        detail="Workspace not found"
    )