"""
v1 bilan moslik: ``Almashtirish`` klassi hamon ishlaydi (DeprecationWarning bilan)
va v1 README’dagi to‘g‘ri natijalar saqlanib qolgan.
"""

import pytest

from LotinKrillYangiLotin import Almashtirish

pytestmark = pytest.mark.filterwarnings("ignore::DeprecationWarning")


@pytest.fixture(scope="module")
def a():
    return Almashtirish()


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
        ("YangiLotinga", "shamol", "şamol"),
    ],
)
def test_v1_readme_misollari(a, usul, kirish, kutilgan):
    assert getattr(a, usul)(kirish) == kutilgan


@pytest.mark.parametrize("apostrof", ["'", "`", "ʻ", "ʼ", "’", "‘"])
def test_v1_apostrof_variantlari_krillga(a, apostrof):
    assert a.Krillga(f"o{apostrof}g{apostrof}il") == "ўғил"


def test_almashtirish_eskirgan_ogohlantirish():
    with pytest.warns(DeprecationWarning, match="to_new_latin"):
        Almashtirish().YangiLotinga("choy")
