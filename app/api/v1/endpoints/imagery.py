from fastapi import APIRouter, Query
from typing import Optional
from app.services.gibs import get_layer_tile
from app.services.tiles import deg2num

router = APIRouter()


def get_tile_response(
        layer: str,
        z: int,
        x: Optional[int],
        y: Optional[int],
        lat: Optional[float],
        lon: Optional[float],
        date: Optional[str],
):
    if lat is not None and lon is not None:
        x, y = deg2num(lat, lon, z)
    elif x is None or y is None:
        return {"error": "Either provide x and y or lat and lon"}

    url = get_layer_tile(layer, z, x, y, date)
    return {"tile_url": url}


@router.get("/clouds")
def get_cloud_tile(
        z: int = Query(5, ge=0, le=9),
        x: Optional[int] = None,
        y: Optional[int] = None,
        lat: Optional[float] = None,
        lon: Optional[float] = None,
        date: Optional[str] = None,
):
    return get_tile_response("MODIS_Terra_Cloud_FR", z, x, y, lat, lon, date)


@router.get("/fires")
def get_fire_tile(
        z: int = Query(5, ge=0, le=9),
        x: Optional[int] = None,
        y: Optional[int] = None,
        lat: Optional[float] = None,
        lon: Optional[float] = None,
        date: Optional[str] = None,
):
    return get_tile_response("VIIRS_SNPP_Thermal_Anomalies_NRT", z, x, y, lat, lon, date)


@router.get("/no2")
def get_no2_tile(
        z: int = Query(5, ge=0, le=9),
        x: Optional[int] = None,
        y: Optional[int] = None,
        lat: Optional[float] = None,
        lon: Optional[float] = None,
        date: Optional[str] = None,
):
    return get_tile_response("TROPOMI_NO2", z, x, y, lat, lon, date)


@router.get("/co")
def get_co_tile(
        z: int = Query(5, ge=0, le=9),
        x: Optional[int] = None,
        y: Optional[int] = None,
        lat: Optional[float] = None,
        lon: Optional[float] = None,
        date: Optional[str] = None,
):
    return get_tile_response("TROPOMI_CO", z, x, y, lat, lon, date)

