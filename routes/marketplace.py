from fastapi import APIRouter

router = APIRouter(
    prefix="/marketplace",
    tags=["marketplace"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/job")
def add_job():
    job_id = 1
    return job_id


@router.get("/matches/{job_id}")
def get_matches(job_id: int):
    return {"Hello": "World"}
