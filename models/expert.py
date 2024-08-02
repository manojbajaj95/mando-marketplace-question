from typing import Optional

from sqlmodel import Field, SQLModel


class Expert(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
