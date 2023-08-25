from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


users = Table(
   "users",
    meta,
    Column("userid", Integer, primary_key=True),
    Column("username", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("address", String(255)),  # Thêm cột address kiểu Text
    Column("phone_number", String(255)),  # Thêm cột phone_number kiểu String
    Column("role", Integer),  # Thêm cột role kiểu Integer
    Column("status", Integer, default=1), 
)

meta.create_all(engine)
