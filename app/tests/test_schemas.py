import pytest
from pydantic import ValidationError
from app.schemas.document import DocumentCreate

def test_validdocument():
    document=DocumentCreate(
    filename="resume.pdf",
    content_type="application/pdf"
    )
    assert document.filename == "resume.pdf"

def test_trimeddocument():
    document=DocumentCreate(
        filename="  resume.pdf  ",
        content_type="application/pdf"
        )
    assert document.filename == "resume.pdf"

def test_fileempty():
    with pytest.raises(ValidationError):
        DocumentCreate(
            filename=" ",
            content_type="application/pdf"
            )
def test_invalid_content_type_fails():
    with pytest.raises(ValidationError):
        DocumentCreate(
            filename="resume.pdf",
            content_type="application/json"
        )
