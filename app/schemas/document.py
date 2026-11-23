from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, field_validator
from typing import Literal

class DocumentCreate(BaseModel):
    filename:str=Field(
        min_length=1,
        max_length=255,
        description="original document filename"
        )
    content_type:Literal[
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain"
        ]
    @field_validator("filename")
    @classmethod

    def validate_filename(cls,value:str)->str:
        value=value.strip()

        if not value:
            raise ValueError("Filename cannot be empty")
        if "/" in value or "\\" in value:
            raise ValueError("Filename must not contain a path")

        return value

class DocumentResponse(BaseModel):
    id:UUID
    Filename: str
    content_type: str
    status: Literal[
        "uploaded",
        "processing",
        "completed",
        "failed"
        ]
    creted_at: datetime
