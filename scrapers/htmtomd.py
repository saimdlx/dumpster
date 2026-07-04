import argparse
import json
import shutil
import subprocess
import sys
import os
import markdownify
from pathlib import Path
from html import unescape
from urllib.parse import unquote
from bs4 import BeautifulSoup

OUT_DIR = Path("mddoc")
SRC_DIR = Path("sldworks")


def link_mids(src_dir = SRC_DIR, out_dir=OUT_DIR):
    return

def iter_htm_files(src_dir=SRC_DIR, out_dir=OUT_DIR):
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for path in sorted(src_dir.glob("*.htm")):
        html = path.read_text(encoding="utf-8", errors="replace")
        md = markdownify.markdownify(html, heading_style="ATX")
        out_path = out_dir / (path.stem + ".md")
        out_path.write_text(md, encoding="utf-8")
        written.append(out_path.name)
    return written

def cleanup(src_dir = SRC_DIR):
    toDel = []
    for path in sorted(src_dir.glob("*.image")):
        try:
            os.remove(path)
        except OSError as e:
            print(f"Could not delete desired file: {e}")

def main():
    md = iter_htm_files()
    

if __name__ == "__main__":
    main()
