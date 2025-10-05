import csv, io
from typing import List, Dict

def csv_to_items(csv_text: str, meta: Dict) -> List[Dict]:
    r = csv.DictReader(io.StringIO(csv_text))
    items = []
    for row in r:
        # Campos varían según ts_type; sé defensivo
        year = int(row.get("year") or row.get("Year") or meta["years"][0])
        month = row.get("month") or row.get("Month")
        date = row.get("date") or row.get("Date")
        value = float(row.get("value") or row.get("ndvi") or row.get("NDVI") or 0.0)
        rid = row.get("id") or row.get("adm_id") or meta.get("region_hint","UNKNOWN")

        period = date or (f"{year}-{int(month):02d}" if month else f"{year}")
        items.append({
            "region_id": f"{meta['shape']}:{rid}",
            "timestamp": period,                  # SK
            "sat": meta["sat"],
            "layer": meta["layer"],
            "ts_type": meta["ts_type"],
            "year": year,
            "value": round(value, 4),
            "meta": {"mask": meta.get("mask"), "version": meta.get("version")}
        })
        return items