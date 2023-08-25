from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends, FastAPI
# config/db.py

from sqlalchemy import MetaData

meta = MetaData()

# Các cấu hình khác của cơ sở dữ liệu


DATABASE_URL = "mysql://root@localhost:3306/b"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# Hàm để lấy Session từ cơ sở dữ liệu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        
        db.close()
conn = engine.connect()


