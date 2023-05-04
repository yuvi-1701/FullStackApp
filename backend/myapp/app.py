from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sqlite3
import csv

from myapp.database.db import engine
from myapp.routes import measurements
from myapp.database.base import Base


app = FastAPI(orm_mode=True)


app.include_router(measurements.router)

# configure CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    # Create the tables in the database using the models defined in the app
    Base.metadata.create_all(bind=engine)

    # Populate the databse with given csv file
    conn = sqlite3.connect("site.db")
    cursor = conn.cursor()

    # Open the CSV file and insert the data into the database
    with open("myapp\database\measurements.csv", "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            cursor.execute(
                "INSERT INTO male_measurements (height, weight, age, waist) VALUES (?, ?, ?, ?)",
                row,
            )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


@app.on_event("shutdown")
async def tear_down():
    conn = sqlite3.connect("site.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM male_measurements")

    conn.commit()
    conn.close()
