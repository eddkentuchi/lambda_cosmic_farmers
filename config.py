
import os

GLAM_URL = os.getenv("GLAM_URL", "https://glam1.gsfc.nasa.gov/api/gettbl/v4")
DDB_TABLE = os.getenv("DDB_TABLE", "glam_timeseries")
RAW_BUCKET = os.getenv("RAW_BUCKET", "")   # opcional
TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "60"))
BATCH_IDS = int(os.getenv("BATCH_IDS", "50"))  # particiona ids si tienes muchos
DEFAULT = {
    "version": "v16.1",
    "sat": "MOD",
    "layer": "NDVI",
    "mask": "USGS-NLCD_2021_crops",
    "shape": "ADM",
    "ids": ["110955","110961"],
    "years": [2023, 2024],
    "ts_type": "seasonal",
    "start_month": 4,
    "num_months": 8,
    "format": "csv"
}