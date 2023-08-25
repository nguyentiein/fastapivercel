# from sqlalchemy import text
# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from config.db import get_db

# app = FastAPI()

# @app.get("/test-db")
# async def test_db(db: Session = Depends(get_db)):
#     # Perform a query to retrieve all user records from the "users" table
#     query = text("SELECT * FROM users")
#     result = db.execute(query)

#     # Fetch all rows and convert them to a list of dictionaries
#     user_records = []
#     for row in result:
#         record = {
#             "id": row[0],    # Replace with the correct index for the 'id' column
#             "name": row[1],  # Replace with the correct index for the 'name' column
#             "age": row[2],   # Replace with the correct index for the 'age' column
#             # ... Add more columns as needed
#         }
#         user_records.append(record)

#     return {"users": user_records}


