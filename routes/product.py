# @productss.get(
#     "/products",
#     tags=["products"],
#     response_class=HTMLResponse,
#     description="Get a list of all products",
# )

# def get_products(request: Request):
#     products_list = conn.execute(select(products)).fetchall()
#     return templates.TemplateResponse("shop.html", {"request": request, "product_list": products_list})

# @productss.get(
#     "/products",
#     tags=["products"],
#     response_class=HTMLResponse,
#     description="Get a list of all products",
# )


# @productss.get("/products", response_class=HTMLResponse)
# def read_products(skip: int = Query(0, alias="offset"), limit: int = Query(2, alias="page_size")):
#     query = select(products).offset(skip).limit(limit)
#     result = conn.execute(query)
#     products_list = result.fetchall()

#     # Render template
#     template = templates.get_template("shop.html")
#     rendered_content = template.render(product_list=products_list)

#     return HTMLResponse(content=rendered_content)

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.sql import select
from config.db import conn, get_db
from models.product import products
from schemas.product import Product
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles 
from sqlalchemy import desc
from sqlalchemy import asc
from fastapi import FastAPI, Query, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.sql import select, text
from sqlalchemy.orm import Session
from sqlalchemy_pagination import paginate
from config.db import conn, engine
from models.product import products
from schemas.product import Product
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, Request, Depends




from sqlalchemy import text
from typing import List



from models.product import products

import logging

app = FastAPI()
templates = Jinja2Templates(directory="assets/templates")
cart = []
# Mount the static directory
app.mount("/assets", StaticFiles(directory="assets/"), name="static")


productss = APIRouter()


@productss.get("/products", response_class=HTMLResponse)
def read_products(request: Request, skip: int = Query(1, alias="offset"), limit: int = Query(2, alias="page_size"), db: Session = Depends(get_db)):
    query = select(products).offset(skip).limit(limit)
    result = db.execute(query)
    products_list = result.fetchall()

    # Render template
    template = templates.get_template("shop.html")

    # Calculate previous and next offsets
    prev_offset = max(0, skip - limit)
    next_offset = skip + limit

    rendered_content = template.render(
        request=request,
        product_list=products_list,
        prev_offset=prev_offset,
        next_offset=next_offset,
    )

    return HTMLResponse(content=rendered_content)



def get_products(request: Request):
    products_list = conn.execute(select(products)).fetchall()

    # Log products list
    logging.info("Products list: %s", products_list)

    # Render template
    template = templates.get_template("shop.html")
    rendered_content = template.render(request=request, product_list=products_list)

    # Log rendered content
    logging.info("Rendered content: %s", rendered_content)

    return HTMLResponse(content=rendered_content)



@productss.get("/singleproduct/shop-cart", response_class=HTMLResponse)
async def shop_cart(request: Request):
    
    return templates.TemplateResponse("shop-cart.html", {"request": request})
#singleproduct




@productss.get("/singleproduct", response_class=HTMLResponse)
async def shop_cart(request: Request):
    return templates.TemplateResponse("single-product.html", {"request": request})


@productss.get("/singleproduct/{productid}")
async def shop_cart(request: Request, productid: str):
    # Thực hiện truy vấn để lấy thông tin sản phẩm từ cơ sở dữ liệu
    stmt = select(products).where(products.c.product_id == productid)
    query_result = conn.execute(stmt).fetchone()

    if query_result is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # Tạo đối tượng Product từ kết quả truy vấn
    product = Product(
        product_id=query_result.product_id,
        name=query_result.name,
        description=query_result.description,
        price=query_result.price,
        image=query_result.image,
        category_id=query_result.category_id,
        title=query_result.title,
        discount=query_result.discount
    )

    return templates.TemplateResponse("single-product.html", {"request": request, "product": product})







@productss.get(
    "/search",
    tags=["products"],
    response_class=HTMLResponse,
    description="Search products",
)
def search_products(request: Request, query: str):
    query = f"%{query}%"  # Add wildcards to the query for partial matching
    products_list = conn.execute(select(products).where(products.c.name.ilike(query))).fetchall()
    return templates.TemplateResponse("shop.html", {"request": request, "query": query, "product_list": products_list})



@productss.get("/sort", tags=["products"], response_class=HTMLResponse, description="Sort products")
def sort_products(request: Request, sort: str):
    # Xử lý sắp xếp sản phẩm dựa trên giá
    if sort == "low_to_high":
        query = select(products).order_by(text("products.price ASC"))  # Sử dụng text() và ASC
    elif sort == "high_to_low":
        query = select(products).order_by(text("products.price DESC"))  # Sử dụng text() và DESC
    else:
        # Mặc định hoặc trường hợp không xác định
        query = select(products)
    
    sorted_products = conn.execute(query).fetchall()
    
    return templates.TemplateResponse("shop.html", {"request": request, "product_list": sorted_products})






cart: List[Product] = []
@productss.get("/add-to-cart/{productid}", response_class=HTMLResponse)
async def add_to_cart(request: Request, productid: int):
    stmt = select(products).where(products.c.product_id == productid)
    query_result = conn.execute(stmt).fetchone()

    if query_result is None:
        raise HTTPException(status_code=404, detail="Product not found")



    # Tạo đối tượng Product từ kết quả truy vấn
    product = Product(
        product_id=query_result.product_id,
        name=query_result.name,
        description=query_result.description,
        price=query_result.price,
        image=query_result.image,
        category_id=query_result.category_id,
        title=query_result.title,
        discount=query_result.discount
    )

    # Thêm sản phẩm vào giỏ hàng
    cart.append(product)

    # Chuyển hướng đến trang giỏ hàng
    return templates.TemplateResponse("shop-cart.html", {"request": request, "cart": cart})




@productss.get("/ordernow", response_class=HTMLResponse)
async def ordernow(request: Request, productid: int):
    stmt = select(products).where(products.c.product_id == productid)
    query_result = conn.execute(stmt).fetchone()

    if query_result is None:
        raise HTTPException(status_code=404, detail="Product not found")

    product = Product(
        product_id=query_result.product_id,
        name=query_result.name,
        description=query_result.description,
        price=query_result.price,
        image=query_result.image,
        category_id=query_result.category_id,
        title=query_result.title,
        discount=query_result.discount
    )

    return templates.TemplateResponse("order.html", {"request": request, "product": product})




    












