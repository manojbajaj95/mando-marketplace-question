from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/expert",
    tags=["experts"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/profile")
def profile():
    "Experts can create professional profiles"
    return {"Hello": "World"}


@router.get("/availability")
def getAvailability():
    return {"Hello": "World"}


@router.post("/availability")
def setAvailability():
    return {"Hello": "World"}
