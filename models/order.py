from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, Float, String, DateTime
from config.db import meta, engine




orders = Table(
    "orders",
    meta,
    Column("order_id", Integer, primary_key=True,autoincrement=True),
    Column("userid", Integer),
    Column("staff_id", Integer),
    Column("state", Integer),
    Column("total", Float),
    Column("orderDate", DateTime),
    Column("product_id", Integer),
    Column("quantity", Integer),
)

meta.create_all(engine)
