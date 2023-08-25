from fastapi import APIRouter, Request, applications, Form
from cryptography.fernet import Fernet
from typing import List
from models.order import orders
from schemas.order import Order
from config.db import conn, get_db
from sqlalchemy import func, select
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi import FastAPI, Request, Depends
from fastapi import FastAPI, HTTPException, Request

order = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)




from fastapi import FastAPI, Form, HTTPException, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from sqlalchemy import insert
from datetime import datetime

app = FastAPI()

@order.post("/create", tags=["orders"], description="Create a new order")
def create_order(
    total: float = Form(...),
    product_id: int = Form(...),
    quantity: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        print(orders)  # In ra đối tượng 'orders' để gỡ lỗi
    
        
        ins = orders.insert().values(
          
            userid=1,
            staff_id=1,
            state=1,
            total=total,
            orderDate=datetime.now().date(),
            product_id=product_id,
            quantity=quantity
        )
        
        print(ins)  # In ra đối tượng 'ins' để gỡ lỗi
        
        db.execute(ins)
        db.commit()

        print("Order created successfully")
        return {"message": "Order created successfully"}
    except Exception as e:
        db.rollback()
        print("Error:", str(e))
        raise HTTPException(status_code=500, detail="An error occurred")












@order.get("/orders",
            tags=["orders"],
            response_model=List[Order],
            description="Get a list of all orders",
           )
async def get_orders():
    return conn.execute(orders.select()).fetchall()


# @order.post("/create", tags=["orders"], response_model=Order, description="Create a new order")
# def create_order(order: Order):
#     new_order = {
#         "order_id": None,  # Hoặc một giá trị mặc định khác nếu cần
#     "userid": None,
#     "staff_id": None,
#     "state": None,
#         "total": float(order.total),
#         "orderDate":  datetime.now().date(),
#         "product_id": int(order.product_id),  
#         "quantity": int(order.quantity),  
#     }
#     result = conn.execute(orders.insert().values(new_order))
#     return conn.execute(orders.select().where(orders.c.order_id == result.lastrowid)).first()

# @order.post("/create", tags=["orders"], response_model=Order, description="Create a new order")
# def create_order():
#         return {"message": "Information received successfully"}
#     total: float = Form(...),

#     product_id: int = Form(...),
#     quantity: int = Form(...)
# ):
#     print("Total:", total)
    
#     print("Product ID:", product_id)
#     print("Quantity:", quantity)
 





# app = FastAPI()

# @app.post("/create", tags=["orders"], description="Create a new order")
# def create_order(
#     total: float = Form(...),
#     orderDate: str = Form(...),
#     product_id: int = Form(...),
#     quantity: int = Form(...)
# ):
#     # Xử lý dữ liệu tại đây
#     return {"message": "Order information received successfully"}

    



