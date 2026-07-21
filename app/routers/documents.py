from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID, uuid4

from app.schemas import DocumentIn, DocumentOut
from app.storage import workspaces, documents

router = APIRouter()


router = APIRouter()

@router.post('/documents', response_model=DocumentOut, tags=['Documents'])
def create_document(doc: DocumentIn,):
    for workspace in workspaces:
        if workspace.id == doc.workspace_id:
            break
    else:
        raise HTTPException(
            status_code=404,
            detail="Workspace not found"
        )

    data = DocumentOut(
        id=uuid4(),
        **doc.model_dump()
    )

    documents.append(data)
    return data


@router.get(
    "/workspaces/{workspace_id}/documents",
    response_model=List[DocumentOut],
    tags=["Documents"]
)
def get_workspace_documents(workspace_id: UUID):
    workspace_documents = []
    for document in documents:
        if document.workspace_id == workspace_id:
            workspace_documents.append(document)
    return workspace_documents

@router.get(
    "/documents/{document_id}",
    response_model=DocumentOut,
    tags=["Documents"]
)
def get_document(document_id: UUID):
    for document in documents:
        if document.id == document_id:
            return document

    raise HTTPException(
        status_code=404,
        detail="Document not found"
    )