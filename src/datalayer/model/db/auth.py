from sqlmodel import SQLModel, Field, Table, table, true
from sqlalchemy import Column, DateTime, JSON
from uuid import UUID
from datetime import datetime, timezone
from typing import Optional

class RoleDB(SQLModel, table=True):
    __tablename__ = "auth"
    __table_args__ = {"schema": "public"}
