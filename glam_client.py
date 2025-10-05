import urllib.parse, urllib.request
from config import GLAM_URL, TIMEOUT

def glam_post_csv(params: dict) -> str:
    fields = []
    for k, v in params.items():
        if isinstance(v, list):
            for item in v:
                fields.append((k, str(item)))
        else:
            fields.append((k, str(v)))
    data = urllib.parse.urlencode(fields).encode("utf-8")
    req = urllib.request.Request(GLAM_URL, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        if resp.status != 200:
            raise RuntimeError(f"GLAM HTTP {resp.status}")
        return resp.read().decode("utf-8")