import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, MetaData, Integer, ForeignKey, String, Date, Column
from sqlalchemy.orm import DeclarativeBase, relationship, Session
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

DATBASE_URL = "sqllite:///demo.db"