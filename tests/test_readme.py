"""README’dagi misollar va "Murakkab holatlar" jadvali kod bilan mos kelishini tekshiradi."""

import pathlib
import re

import pytest

import LotinKrillYangiLotin as lky

README = (pathlib.Path(__file__).resolve().parent.parent / "README.md").read_text(encoding="utf-8")
YONALISH = {"Krill": lky.to_cyrillic, "Lotin": lky.to_latin, "Yangi lotin": lky.to_new_latin}


def _murakkab_holatlar():
    m = re.search(r"<!-- murakkab-holatlar:boshi -->(.*?)<!-- murakkab-holatlar:oxiri -->", README, re.S)
    assert m, "README’da murakkab holatlar jadvali topilmadi"
    qatorlar = []
    for qator in m.group(1).strip().splitlines()[2:]:  # sarlavha va ajratgichdan keyin
        ustunlar = [u.strip() for u in qator.strip().strip("|").split("|")]
        kirish, yonalish, natija = ustunlar[0].strip("`"), ustunlar[1], ustunlar[2].strip("`")
        qatorlar.append((kirish, yonalish, natija))
    return qatorlar


MURAKKAB = _murakkab_holatlar()


def test_jadval_toliq():
    assert len(MURAKKAB) >= 15


@pytest.mark.parametrize("kirish, yonalish, natija", MURAKKAB)
def test_murakkab_holat(kirish, yonalish, natija):
    assert YONALISH[yonalish](kirish) == natija


# README’dagi `funksiya("...")  # '...'` ko‘rinishidagi python misollari
_MISOL = re.compile(
    r"""^(?P<f>to_latin|to_cyrillic|to_new_latin|detect_script)\((?P<arg>"[^"]*")(?:,\s*source="(?P<src>\w+)")?\)\s+#\s*'(?P<natija>[^']*)'""",
    re.M,
)
PY_MISOLLAR = [(m["f"], m["arg"][1:-1], m["src"], m["natija"]) for m in _MISOL.finditer(README)]


def test_py_misollar_topildi():
    assert len(PY_MISOLLAR) >= 10


@pytest.mark.parametrize("f, arg, src, natija", PY_MISOLLAR)
def test_py_misol(f, arg, src, natija):
    funksiya = getattr(lky, f)
    natija_haqiqiy = funksiya(arg) if src is None else funksiya(arg, source=src)
    assert natija_haqiqiy == natija


@pytest.mark.parametrize(
    "krill, lotin, yangi",
    [
        ("ўқитувчи", "o‘qituvchi", "öqituvçi"),
        ("ғалаба", "g‘alaba", "ğalaba"),
        ("шаҳар", "shahar", "şahar"),
        ("чой", "choy", "çoy"),
        ("маъно", "ma’no", "ma’no"),
    ],
)
def test_alifbo_jadvali(krill, lotin, yangi):
    assert lky.to_latin(krill) == lotin
    assert lky.to_new_latin(krill) == yangi
    for x in (krill, lotin, yangi):
        assert lky.to_cyrillic(x) == krill
