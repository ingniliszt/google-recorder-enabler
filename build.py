from pathlib import Path
import zipfile, hashlib
root = Path(__file__).resolve().parent
out = root / "dist"
out.mkdir(exist_ok=True)
files = {n: (root / n).read_bytes() for n in ["module.prop", "customize.sh", "system/etc/sysconfig/recorder_pixel_feature_test.xml"]}
dirs = {str(p) + "/" for n in files for p in Path(n).parents if str(p) != "."}
version = next(l.split("=", 1)[1] for l in files["module.prop"].decode().splitlines() if l.startswith("version="))
path = out / f"google-recorder-enabler-v{version}.zip"
with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for n in sorted(dirs | set(files)):
        info = zipfile.ZipInfo(n, (1980, 1, 1, 0, 0, 0))
        info.create_system = 3
        info.external_attr = ((0o40755 if n.endswith("/") else 0o100644) << 16) | (16 if n.endswith("/") else 0)
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, b"" if n.endswith("/") else files[n], compresslevel=9)
digest = hashlib.sha256(path.read_bytes()).hexdigest()
(out / "SHA256SUMS.txt").write_text(digest + "  " + path.name + "\n", encoding="utf-8")
print(path)
