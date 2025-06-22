from datetime import date as dt
from typing import Optional

import httpx
from fastapi import APIRouter, HTTPException, Path, Query
from fastapi.responses import StreamingResponse

router = APIRouter()

LAYER_MAP = {
    "clouds": "MODIS_Terra_Cloud_FR",
    "fires": "VIIRS_SNPP_Thermal_Anomalies_NRT",
    "no2": "TROPOMI_NO2",
    "co": "TROPOMI_CO",
}


@router.get("/api/tiles/clouds/{z}/{x}/{y}.jpg")
async def get_cloud_tile(
    z: int = Path(..., ge=0, le=9),
    x: int = Path(...),
    y: int = Path(...),
    date: Optional[str] = Query(None),
):
    if not date:
        date = dt.today().isoformat()

    nasa_url = (
        f"https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/"
        f"MODIS_Terra_CorrectedReflectance_TrueColor/default/{date}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.jpg"
    )

    async with httpx.AsyncClient() as client:
        resp = await client.get(nasa_url)

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail="Tile not found")

    return StreamingResponse(resp.aiter_bytes(), media_type="image/jpeg")
