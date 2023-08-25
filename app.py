# from fastapi import FastAPI
# from routes.user import user
# from config.openapi import tags_metadata

# app = FastAPI(
#     title="Users API",
#     description="a REST API using python and mysql",
#     version="0.0.1",
#     openapi_tags=tags_metadata,
# )

# app.include_router(user)
from config.db import meta 
from fastapi.staticfiles import StaticFiles 
from fastapi import FastAPI, Depends, Form, status, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from models.user import users 
from routes.user import user
from routes.product import productss
from routes.order import order
from models.product import products 
from passlib.hash import bcrypt



from config.db import get_db

app = FastAPI()

# Create Jinja2Templates instance
templates = Jinja2Templates(directory="assets/templates")

# Mount the static directory
app.mount("/assets", StaticFiles(directory="assets/"), name="static")


@app.get("/s", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
                return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        print("Template rendering error:", e)

@app.get("/login_index", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("account-login.html", {"request": request})


# Function to authenticate user
def authenticate_user(db: Session, username1: str, password: str):
    query = select(users).where(users.c.username == username1)

    user = db.execute(query).fetchone()

    if user and user.password == password:
        print("Password verification successful")
        return True
    else:
        print("Password verification failed")
        return False
    



# Endpoint to handle login form submission
@app.post("/login", response_class=RedirectResponse)
async def login_post(request: Request, username1: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    authenticated = authenticate_user(db, username1, password)

    if authenticated:
        return RedirectResponse(url="products", status_code=status.HTTP_303_SEE_OTHER)  # Use status_code to specify redirection status
    else:         
         return templates.TemplateResponse("shop.html", {"request": request})
    

app.get("/shop.html", response_class=HTMLResponse)
def show_shop(request: Request):
    # Process data for the shop page (replace with your logic)
    shop_data = "Shop data"  # Replace with your logic

    return templates.TemplateResponse("shop.html", {"request": request, "shop_data": shop_data})
    

    
app.include_router(productss)
app.include_router(user)

app.include_router(order)










