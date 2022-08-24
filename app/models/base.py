from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func, text

import uuid
from typing import Optional

class BaseModel(SQLModel):
    id: Optional[int] = Field(
        default=None, 
        primary_key=True,
        index=True,
        nullable=False
    )
    created_at: Optional[int] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=func.now()
        )
    )
    updated_at: Optional[int] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            onupdate=func.now(),
            server_default=func.now()
        )
    )

class UUIDBaseModel(BaseModel):
    id: Optional[uuid.UUID] = Field(
        sa_column=Column(
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            server_default=text('gen_random_uuid()'),
            index=True,
            nullable=False
        )
    )