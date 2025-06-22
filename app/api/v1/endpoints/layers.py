import json
from pathlib import Path

from fastapi import APIRouter

router = APIRouter()


@router.get("/layers")
def get_layers():
    file_path = Path("app/data/layers.json")
    if not file_path.exists():
        return {"error": "layers.json not found"}
    return json.loads(file_path.read_text(encoding="utf-8"))
