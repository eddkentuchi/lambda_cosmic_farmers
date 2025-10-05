import json, time
from config import DEFAULT, RAW_BUCKET
from glam_client import glam_post_csv
from parser import csv_to_items
from ddb import put_items
import boto3

s3 = boto3.client("s3") if RAW_BUCKET else None

def lambda_handler(event, context):
    params = {**DEFAULT, **(event.get("detail") or {})}
    meta = {
        "version": params["version"], "sat": params["sat"], "layer": params["layer"],
        "mask": params.get("mask"), "shape": params["shape"], "ts_type": params["ts_type"],
        "years": params.get("years", []), "region_hint": (params.get("ids") or ["?"])[0]
    }

    csv_text = glam_post_csv(params)

    if s3:
        key = f"glam/{meta['sat']}/{meta['shape']}/run_{int(time.time())}.csv"
        s3.put_object(Bucket=RAW_BUCKET, Key=key, Body=csv_text.encode("utf-8"))

    items = csv_to_items(csv_text, meta)
    if items:
        put_items(items)

    return {"count": len(items), "params": params}