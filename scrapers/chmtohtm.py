import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from html import unescape
from urllib.parse import unquote
from bs4 import BeautifulSoup

OUT_DIR  = Path("chm_out")
TOC_JSON = Path("toc.json")


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="ignore")


def extract_chm(chm_path: Path, out_dir: Path) -> None:
    if not chm_path.is_file():
        sys.exit(f"Not found")
    out_dir.mkdir(parents=True, exist_ok=True)

    tool = shutil.which("extract_chmLib")
    if tool:
        subprocess.run([tool, str(chm_path), str(out_dir)], check=True)
        return
    sys.exit("No CHM extractor found")


def find_hhc(out_dir: Path) -> Path:
    hhcs = sorted(out_dir.rglob("*.hhc"))
    if not hhcs:
        sys.exit(f"hhc file not found")
    return max(hhcs, key=lambda p: p.stat().st_size) #main table of cont. = largest


def obj_fields(li):
    obj = li.find("object", recursive=False) or li.find("object")
    if obj is None:
        return None, None
    name = local = None
    for param in obj.find_all("param", recursive = False):
        key = (param.get("name") or "").lower()
        val = param.get("value")
        if key == "name" and name is None:
            name = unescape((val or "").strip())
        elif key == "local" and val and local is None:
            local = val
        return name, local
    
def _norm_local(local: str) -> str:
    return unquote(local).split("#")[0].replace("\\","/").strip().lstrip("/")

def parse_hhc(hhc_path: Path) -> list[dict]:
    soup = BeautifulSoup(read_text(hhc_path), "lxml")
    nodes: list[dict] = []
    counter = [0]

    def walk(ul, parent_id, ancestors):
        for li in ul.find_all("li", recursive=False):
            name, local = obj_fields(li)
            if name is None:
                continue
            nid = counter[0]
            counter[0] += 1
            rel = _norm_local(local) if local else None
            heading_path = ancestors + [name]
            nodes.append({
                "id": nid,
                "parent_id": parent_id,
                "title": name,
                "rel_path": rel,
                "heading_path": heading_path,
                "depth": len(ancestors),
            })

            child_ul = li.find("ul", recursive = False)
            if child_ul is not None:
                walk(child_ul, nid, heading_path)

    top_uls = [ul for ul in soup.find_all("ul") if ul.find_parent("ul") is None]
    for ul in top_uls:
        walk(ul, None, [])
    return nodes


def reconcile(nodes: list[dict], out_dir: Path) -> list[str]:
    on_disk = {}
    for p in out_dir.rglob("*.htm"):
        key = str(p.relative_to(out_dir)).replace("\\" , "/").lower()
        on_disk[key] = p

    matched = set()
    for n in nodes:
        rel = n["rel_path"]
        if not rel:
            n["file"] = None
            continue
        p = on_disk.get(rel.lower())
        n["file"] = str(p) if p else None
        if p:
            matched.add(p)

    orphans = [str(p) for k, p in on_disk.items()
               if p not in matched and k.endswith((".htm", ".html"))]
    return sorted(orphans)


def iter_pages(nodes: list[dict]):
    seen = set()
    for n in nodes:
        f = n.get("file")
        if not f or f in seen:
            continue
        seen.add(f)
        try:
            yield n, read_text(Path(f))
        except OSError:
            continue

def main() -> None:
    ap = argparse.ArgumentParser(description="Extract a .chm and emit its topic hierarchy.")
    ap.add_argument("chm", nargs="?", help="path to the .chm file")
    ap.add_argument("--extracted", help="use an already-extracted folder instead of extracting")
    args = ap.parse_args()

    out_dir = Path(args.extracted) if args.extracted else OUT_DIR
    if not args.extracted:
        if not args.chm:
            sys.exit("Provide a .chm path")
        extract_chm(Path(args.chm), out_dir)

    hhc = find_hhc(out_dir)
    nodes = parse_hhc(hhc)
    orphans = reconcile(nodes, out_dir)
    TOC_JSON.write_text(json.dumps(nodes, indent=2, ensure_ascii=False), encoding="utf-8")

    with_path = [n for n in nodes if n["rel_path"]]
    missing = [n for n in with_path if not n["file"]]
    unique_files = {n["file"] for n in nodes if n.get("file")}

    print(f"TOC: {hhc}")
    print(f"  total nodes:            {len(nodes)}")
    print(f"  container nodes (folders): {len(nodes) - len(with_path)}")
    print(f"  topic nodes:            {len(with_path)}")
    print(f"  unique topic files:     {len(unique_files)}")
    print(f"  missing (in TOC, no file on disk): {len(missing)}")
    print(f"  orphan files (on disk, not in TOC): {len(orphans)}")
    print(f"wrote {TOC_JSON}")
 
    # demonstrate the fetch step the rest of the pipeline consumes
    pages = sum(1 for _ in iter_pages(nodes))
    print(f"iter_pages() yields {pages} readable topic pages")
 
 
if __name__ == "__main__":
    main()