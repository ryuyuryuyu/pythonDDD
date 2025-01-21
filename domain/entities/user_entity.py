from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id: int = Field(..., description="Unique identifier for the user")
    name: str = Field(..., description="Name of the user")
    email: EmailStr = Field(..., description="Email address of the user")
    
    class Config:
        allow_mutation = False

# Example usage
user = User(id=1, name="John Doe", email="john.doe@example.com")
print(user)
