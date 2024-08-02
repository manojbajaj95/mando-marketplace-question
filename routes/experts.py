from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from database import get_session
from models.expert import Expert

router = APIRouter(
    prefix="/expert",
    tags=["experts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/profile")
def get_profile(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    session: Session = Depends(get_session),
):
    "Experts can create professional profiles"
    experts = session.exec(select(Expert).offset(offset).limit(limit)).all()
    return experts


@router.post("/profile")
def profile(expert: Expert, session: Session = Depends(get_session)):
    "Experts can create professional profiles"
    session.add(expert)
    session.commit()
    session.refresh(expert)
    return expert


@router.get("/availability")
def getAvailability():
    return {"Hello": "World"}


@router.post("/availability")
def setAvailability():
    return {"Hello": "World"}
