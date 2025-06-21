from datetime import datetime


def format_date(date: str | None = None) -> str:
    if not date:
        return datetime.utcnow().strftime('%Y-%m-%d')
    return date


def get_layer_tile(layer: str, z: int, x: int, y: int, date: str | None = None) -> str:
    date = format_date(date)
    return (
        f"https://gibs.earthdata.nasa.gov/wmts/epsg3857/best/"
        f"{layer}/default/{date}/GoogleMapsCompatible_Level9/{z}/{y}/{x}.png"
    )
