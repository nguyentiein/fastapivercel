from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String, Text, DECIMAL
from config.db import meta, engine

products = Table(
    "products",
    meta,
    Column("product_id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("description", Text, nullable=False),
    Column("price", DECIMAL(10, 2), nullable=False),
    Column("image", String(255), nullable=False),
    Column("category_id", Integer, nullable=False),
    Column("title", String(255)),
    Column("discount", DECIMAL(10, 2)),
)

meta.create_all(engine)
