"""
Veb-demo saytini yig‘ish (GitHub Pages uchun).

    python docs/build.py [CHIQISH_PAPKASI]   # standart: _site

Natija:
    _site/index.html
    _site/py/LotinKrillYangiLotin/*.py   — kutubxonaning aynan o‘zi (src/ dan)
    _site/py/files.json                  — Pyodide yuklashi kerak bo‘lgan fayllar ro‘yxati
    _site/examples.json                  — README’dagi "Murakkab holatlar" jadvali

Lokal ko‘rish:  python docs/build.py && python -m http.server -d _site
"""

from __future__ import annotations

import json
import pathlib
import re
import shutil
import sys

ILDIZ = pathlib.Path(__file__).resolve().parent.parent
PAKET = ILDIZ / "src" / "LotinKrillYangiLotin"
YONALISH = {"Krill": "krill", "Lotin": "lotin", "Yangi lotin": "yangi"}


def murakkab_holatlar(readme: str) -> list[dict]:
    m = re.search(r"<!-- murakkab-holatlar:boshi -->(.*?)<!-- murakkab-holatlar:oxiri -->", readme, re.S)
    if not m:
        raise SystemExit("README’da murakkab holatlar jadvali topilmadi")
    natija = []
    for qator in m.group(1).strip().splitlines()[2:]:
        u = [x.strip() for x in qator.strip().strip("|").split("|")]
        natija.append({
            "kirish": u[0].strip("`"),
            "maqsad": YONALISH[u[1]],
            "natija": u[2].strip("`"),
            "izoh": u[3].replace("`", ""),
        })
    return natija


def versiya() -> str:
    m = re.search(r'__version__ = "([^"]+)"', (PAKET / "__init__.py").read_text(encoding="utf-8"))
    return m.group(1) if m else "?"


def yig(chiqish: pathlib.Path) -> None:
    if chiqish.exists():
        shutil.rmtree(chiqish)
    py = chiqish / "py" / "LotinKrillYangiLotin"
    py.mkdir(parents=True)

    fayllar = []
    for f in sorted(PAKET.glob("*.py")):
        if f.name in ("cli.py", "__main__.py"):
            continue  # brauzerda kerak emas
        shutil.copy2(f, py / f.name)
        fayllar.append(f.name)
    (chiqish / "py" / "files.json").write_text(json.dumps(fayllar), encoding="utf-8")

    readme = (ILDIZ / "README.md").read_text(encoding="utf-8")
    misollar = {"versiya": versiya(), "misollar": murakkab_holatlar(readme)}
    (chiqish / "examples.json").write_text(json.dumps(misollar, ensure_ascii=False, indent=1), encoding="utf-8")

    for f in (ILDIZ / "docs").iterdir():
        if f.is_file() and f.suffix in (".html", ".css", ".js", ".svg", ".ico", ".png"):
            shutil.copy2(f, chiqish / f.name)
    (chiqish / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Sayt yig‘ildi: {chiqish}  ({len(fayllar)} ta py fayl, {len(misollar['misollar'])} ta misol)")


if __name__ == "__main__":
    yig(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ILDIZ / "_site").resolve())
