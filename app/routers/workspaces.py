from fastapi import APIRouter
from app.storage import workspaces, documents
from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID, uuid4
from fastapi import Depends

from app.schemas import WorkspaceIn, WorkspaceOut
from app.dependencies import get_workspace_by_id
from app.storage import workspaces

router = APIRouter()


@router.post("/workspaces", response_model=WorkspaceOut, tags=['Workspace'])
def create_workspace(ws: WorkspaceIn):
    data = WorkspaceOut(
        id=uuid4(),
        **ws.model_dump()
    )
    workspaces.append(data)
    return data


@router.get("/workspaces", response_model=List[WorkspaceOut], tags=['Workspace'])
def get_all_workspaces():
    return workspaces


@router.get("/workspaces/{workspace_id}", tags=['Workspace'])
def get_workspace(
    workspace=Depends(get_workspace_by_id)
):
    return workspace


@router.put("/workspaces/{workspace_id}", response_model=WorkspaceOut, tags=['Workspace'])
def edit_workspace(workspace_id: UUID, ws: WorkspaceIn):
    for index, workspace in enumerate(workspaces):
        if workspace.id == workspace_id:
            updated_workspace = WorkspaceOut(
                id=workspace.id,
                **ws.model_dump()
            )

            workspaces[index] = updated_workspace
            return updated_workspace

    raise HTTPException(
        status_code=404,
        detail="Workspace not found"
    )


@router.delete("/workspaces/{workspace_id}", tags=['Workspace'])
def delete_workspace(workspace_id: UUID):
    for workspace in workspaces:
        if workspace.id == workspace_id:
            workspaces.remove(workspace)
            return {"message": "Workspace deleted successfully."}

    raise HTTPException(
        status_code=404,
        detail="Workspace not found"
    )