"""
1-bosqich testlari.

* ``test_v1_*`` — v1.0.0 ning to‘g‘ri ishlaydigan, saqlanib qolishi kerak bo‘lgan xatti-harakati.
* ``test_malum_xato_*`` — tahlil paytida topilgan xatolar va yangi alifbo (O‘RQ-1184) talablari.
  Ular hozircha ``xfail(strict=True)``: 2-bosqichda yadro qayta yozilgach o‘tishi shart,
  shunda belgini olib tashlash majburiy bo‘ladi.
"""

import pytest

from LotinKrillYangiLotin import Almashtirish


@pytest.fixture(scope="module")
def a():
    return Almashtirish()


# --- v1.0.0 README misollari: saqlanishi kerak ---------------------------------

@pytest.mark.parametrize(
    "usul, kirish, kutilgan",
    [
        ("Lotinga", "функция", "funksiya"),
        ("Krillga", "geometriya", "геометрия"),
        ("Lotinga", "поезд", "poyezd"),
        ("Lotinga", "подъезд", "podyezd"),
        ("Lotinga", "егулик", "yegulik"),
        ("Krillga", "elak", "элак"),
        ("Krillga", "temir", "темир"),
        ("Krillga", "yengil", "енгил"),
        ("Lotinga", "Шу тизимни ўрганиш", "Shu tizimni o‘rganish"),
        ("Krillga", "Shu tizimni o‘rganish", "Шу тизимни ўрганиш"),
        ("Krillga", "ma’no", "маъно"),
        ("Lotinga", "маъно", "ma’no"),
    ],
)
def test_v1_readme_misollari(a, usul, kirish, kutilgan):
    assert getattr(a, usul)(kirish) == kutilgan


@pytest.mark.parametrize("apostrof", ["'", "`", "ʻ", "ʼ", "’", "‘"])
def test_v1_apostrof_variantlari_krillga(a, apostrof):
    assert a.Krillga(f"o{apostrof}g{apostrof}il") == "ўғил"


# --- Ma’lum xatolar va yangi alifbo talablari (2-bosqichda tuzatiladi) ----------

xato = pytest.mark.xfail(strict=True, reason="2-bosqichda tuzatiladi")


@xato
@pytest.mark.parametrize(
    "kirish, kutilgan",
    [
        ("o‘zbek", "özbek"),
        ("G‘ALABA", "ĞALABA"),
        ("ўғил", "öğil"),
        ("Is’hoq", "Ishoq"),
        ("mo‘’tabar", "mö’tabar"),
        ("Чўл", "Çöl"),
    ],
)
def test_malum_xato_yangi_lotin_harflari(a, kirish, kutilgan):
    assert a.YangiLotinga(kirish) == kutilgan


@xato
@pytest.mark.parametrize(
    "usul, kirish, kutilgan",
    [
        ("Krillga", "ketsa aytsa", "кетса айтса"),
        ("Krillga", "Is’hoq", "Исҳоқ"),
        ("Lotinga", "Исҳоқ", "Is’hoq"),
        ("Krillga", "U ‘salom’ dedi", "У ‘салом’ деди"),
        ("Krillga", "(ertak)", "(эртак)"),
        ("Lotinga", "мебель", "mebel"),
        ("Lotinga", "ШАҲАР ва", "SHAHAR va"),
        ("Lotinga", "ПОЕЗД ва", "POYEZD va"),
        ("Krillga", "Öğil", "Ўғил"),
        ("Lotinga", "Öğil", "O‘g‘il"),
    ],
)
def test_malum_xato_qoidalar(a, usul, kirish, kutilgan):
    assert getattr(a, usul)(kirish) == kutilgan
