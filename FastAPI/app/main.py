from email.policy import default

from fastapi import FastAPI,HTTPException, Path,Query
from service.products import get_all_products
from schema.product import ProductCreateRequest

app=FastAPI()

@app.get("/")
def root():
    return {"message":"learning fastapi"} 


@app.get("/products")
def products():
    return get_all_products()
@app.get("/products/list")

def list_products(name:str=Query(default=None,
                                    min_length=1,max_length=50,
                                    description="get products by name(case insensitive)"),

                                    sort_by_price:bool=Query(default=None,description="sort by price"),
                                    order:str=Query(default="asc",description="sort order when sort_by_price=true (asc,desc)"),

                                    limit:int=Query(default=10,ge=1,le=100,description="max products returned"),

                                    offset:int=Query(default=0,ge=0,description="offset for pagination")

                                    ):
    products=get_all_products()
    if name:
        needle=name.strip().lower()
        products=[p for p in products if needle in p.get("name").lower()]
    if not products:
        raise HTTPException(status_code=404,detail="No products found")

    if sort_by_price:
        reverse=order=="desc"
        products=sorted(products,key=lambda x:x.get("price"),reverse=reverse)

    total=len(products)
    products=products[offset:offset+limit]

    return {"total":total,"items":products}

@app.get("/products/{product_id}")

def get_product_by_id(product_id:str= Path(
    ...,
    min_length=36,
    max_length=50,
    description="uuid of the product",
    example="0005a4ea-ce3f-4dd7-bee0-f4ccc70fea6a")
    ):

    products=get_all_products()
    for product in products:
        if product["id"]==product_id:
            return product
    raise HTTPException(status_code=404,detail="Product not found")

@app.post("/products" , status_code=201)


def create_products(Product:ProductCreateRequest):
    return Product.model_dump(mode="json")
