from fastapi import APIRouter

router = APIRouter()


@router.get("/plants/", tags=["plants"])
async def read_plants():
    return [{"name": "flower"}, {"name": "grass"}]
