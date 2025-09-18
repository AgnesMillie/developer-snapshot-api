from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
def check_health():
    """
    Endpoint to check the operational status of the API.
    Returns a simple JSON indicating the service is running.
    """
    return {"status": "ok"}
