"""5-bosqich: veb-demo saytini yig‘ish (docs/build.py)."""

import importlib.util
import json
import pathlib

import LotinKrillYangiLotin as lky

ILDIZ = pathlib.Path(__file__).resolve().parent.parent


def _build_moduli():
    spec = importlib.util.spec_from_file_location("demo_build", ILDIZ / "docs" / "build.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_sayt_yigiladi(tmp_path):
    chiqish = tmp_path / "_site"
    _build_moduli().yig(chiqish)

    assert (chiqish / "index.html").is_file()
    assert (chiqish / ".nojekyll").is_file()

    fayllar = json.loads((chiqish / "py" / "files.json").read_text(encoding="utf-8"))
    assert {"__init__.py", "core.py", "lugat.py"} <= set(fayllar)
    assert "cli.py" not in fayllar
    for nom in fayllar:
        # demo kutubxonaning aynan o‘zini ishlatadi
        assert (chiqish / "py" / "LotinKrillYangiLotin" / nom).read_bytes() == \
            (ILDIZ / "src" / "LotinKrillYangiLotin" / nom).read_bytes()

    d = json.loads((chiqish / "examples.json").read_text(encoding="utf-8"))
    assert d["versiya"] == lky.__version__
    f = {"krill": lky.to_cyrillic, "lotin": lky.to_latin, "yangi": lky.to_new_latin}
    assert len(d["misollar"]) >= 15
    for x in d["misollar"]:
        assert f[x["maqsad"]](x["kirish"]) == x["natija"]


def test_index_html_fayl_nomlariga_mos():
    html = (ILDIZ / "docs" / "index.html").read_text(encoding="utf-8")
    for kerak in ("examples.json", "py/files.json", "py/LotinKrillYangiLotin/", "loadPyodide",
                  "to_new_latin", "to_latin", "to_cyrillic", "detect_script"):
        assert kerak in html
