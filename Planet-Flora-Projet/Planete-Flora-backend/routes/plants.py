from fastapi import APIRouter

router = APIRouter()

plants = [
    {
        "title": "Monstera deliciosa",
        "country": "Mexique",
        "price": 35
    },
    {
        "title": "Ficus lyrata",
        "country": "Afrique",
        "price": 42
    },
    {
        "title": "Lavande",
        "country": "France",
        "price": 12
    }
]


@router.get("/data")
def data(limit: int = 20):
    return plants[:limit]


@router.get("/country/{country}")
def country(country: str):
    return [
        p for p in plants
        if p["country"].lower() == country.lower()
    ]