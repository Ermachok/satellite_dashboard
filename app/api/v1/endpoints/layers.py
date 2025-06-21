from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

@router.get("/layers")
def get_layers():
    file_path = Path("app/data/layers.json")
    if not file_path.exists():
        return {"error": "layers.json not found"}
    return json.loads(file_path.read_text(encoding="utf-8"))
