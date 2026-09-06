from pydantic import BaseModel, Field, AnyUrl,model_validator,computed_field,field_validator
from typing import Annotated , Literal,Optional,List
from uuid import UUID
from datetime import datetime


class ProductCreateRequest(BaseModel):
    name:Annotated[str,Field(min_length=1,max_length=50,description="name of the product",example=["Xiaomi Model Pro","Apple Model Pro"])]
    sku:Annotated[str,Field(min_length=3,max_length=20,description="sku of the product",example="XIQO-354GB-000")] 
    id:UUID
    category:Annotated[str,Field(min_length=3,max_length=50,description="category like electronics/assessoriese etc",example="electronics")]
    brand:Annotated[str,Field(min_length=1,max_length=50,description="brand of the product",example="Xiaomi")]
    price:Annotated[float,Field(gt=0, strict=True,description="price of the product",example=10000.00)]
    currency:Literal["INR"]="INR"
    discount_percent:Annotated[int,Field(ge=0,le=100,description="discount percent on the product",example=10)]
    is_active:Annotated[bool,Field(description="product is active or not",)]
    stock:Annotated[int,Field(ge=0,description="stock of the product",example=100)]
    rating:Annotated[float,Field(ge=0,le=5,strict=True,description="rating of the product",example=4.5)]
    tags:Annotated[Optional[list[str]],Field(description="tags for the product",example=["electronics","mobile"])]
    image_url:Annotated[List[AnyUrl],Field(max_length=5,description="image urls for the product",example=["https://example.com/image1.jpg","https://example.com/image2.jpg"])]

    #dimensions_cm
    #seller

    created_at:datetime

    @field_validator("sku",mode="after")
    @classmethod
    def validate_sku(cls,value:str):
        if "-" not in value:
            raise ValueError("sku must contain '-'")
        last_part=value.split("-")[-1]
        if len(last_part)<3:
            raise ValueError("last part of sku must be at least 3 characters long like -124")
        return value

 
    @model_validator(mode="after")
    def validate_product(cls,model:"ProductCreateRequest"):
        if model.stock==0 and model.is_active is True:
            raise ValueError("product cannot be active if stock is 0")
        if model.discount_percent>0 and model.rating == 0:
            raise ValueError("product cannot have discount if rating is 0")
        return model
    
    @computed_field
    @property
    def discounted_price(self) -> float:
        return round(
        self.price * (1 - self.discount_percent / 100),
        2
    )
        

