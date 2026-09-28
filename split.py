"""Split a build into <=45 MiB parts and record it in builds.json (the site reassembles it).

    python3 split.py <id> <file> [label]
e.g. python3 split.py 13.3.0-android MinionRushRevived-13.3.0.apk
"""
import datetime, hashlib, json, os, sys

PART = 45 * 1024 * 1024
HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "builds.json")

bid, src = sys.argv[1], sys.argv[2]
name = os.path.basename(src)
out = os.path.join(HERE, "builds", bid)
os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    os.remove(os.path.join(out, f))

whole, parts = hashlib.sha256(), []
with open(src, "rb") as f:
    while chunk := f.read(PART):
        whole.update(chunk)
        p = f"{name}.{len(parts):03d}"
        open(os.path.join(out, p), "wb").write(chunk)
        parts.append({"file": f"builds/{bid}/{p}", "size": len(chunk), "sha256": hashlib.sha256(chunk).hexdigest()})

builds = json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}
builds[bid] = {**{k: v for k, v in builds.get(bid, {}).items() if k not in ("name", "size", "sha256", "parts")}, "name": name, "build": builds.get(bid, {}).get("build", 0) + 1,
               "released": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "size": os.path.getsize(src), "sha256": whole.hexdigest(), "parts": parts}
json.dump(dict(sorted(builds.items())), open(MANIFEST, "w"), indent=1)
print(bid, name, len(parts), "parts")
