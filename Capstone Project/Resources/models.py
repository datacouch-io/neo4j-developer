from pydantic import BaseModel, Field

class Customer(BaseModel):
    customer_id: str = Field(..., example="C12345")
    age: int = Field(..., example=30)
    gender: str = Field(..., example="M")

class Merchant(BaseModel):
    merchant_id: str = Field(..., example="M123")
    category: str = Field(..., example="travel")
    zipMerchant: str = Field(..., example="94107")  # ✅ Add this

class Transaction(BaseModel):
    customer_id: str
    merchant_id: str
    amount: float
    step: int
    category: str
    fraud: int

