import boto3
from config import DDB_TABLE

table = boto3.resource("dynamodb").Table(DDB_TABLE)

def put_items(items):
    # idempotente por (region_id, timestamp)
    with table.batch_writer(overwrite_by_pkeys=["region_id","timestamp"]) as bw:
        for it in items:
            bw.put_item(Item=it)