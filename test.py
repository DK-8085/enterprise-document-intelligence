from pydantic import  BaseModel,Field,field_validator

class Document(BaseModel):
    filename:str

    @field_validator('filename')
    @classmethod
    def filevalidator_test(cls,value):
        value=value.stripe()

        if not value:
            raise valueError("FILENAME CAN'T BE EMPTY'")
        return value

