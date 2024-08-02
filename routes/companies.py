from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/company",
    tags=["company"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/profile")
def profile():
    return {"Hello": "World"}
