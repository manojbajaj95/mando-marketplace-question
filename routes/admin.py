from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/utilization")
def utilization():
    return {"Hello": "World"}

