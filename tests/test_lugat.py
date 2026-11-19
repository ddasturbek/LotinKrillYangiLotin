"""3-bosqich: istisnolar lug‘ati."""

import pytest

from LotinKrillYangiLotin import to_cyrillic, to_latin, to_new_latin
from LotinKrillYangiLotin.lugat import KRILL_LOTIN, LOTIN_KRILL


@pytest.mark.parametrize(
    "lotin, krill",
    [
        ("sentabr", "сентябрь"),
        ("Sentabr", "Сентябрь"),
        ("SENTABR", "СЕНТЯБРЬ"),
        ("15-sentabrda", "15-сентябрда"),  # qo‘shimcha bilan ь tushadi
        ("oktabr", "октябрь"),
        ("mebel", "мебель"),
        ("mebellar", "мебеллар"),
        ("sirk", "цирк"),
        ("sirkda", "циркда"),
        ("sirkchi", "циркчи"),
        ("kompyuter", "компьютер"),
        ("kompyuterlarimizda", "компьютерларимизда"),
        ("film", "фильм"),
        ("filmlar", "фильмлар"),
        ("stansiyada", "станцияда"),
        ("konsert", "концерт"),
        ("mer", "мэр"),
        ("epilepsiya", "эпилепсия"),
    ],
)
def test_lotindan_krillga(lotin, krill):
    assert to_cyrillic(lotin) == krill


@pytest.mark.parametrize(
    "lotin, krill",
    [
        ("sirka", "сирка"),     # sirka (сирка) ≠ sirk + a
        ("meros", "мерос"),     # mer o‘zagi, lekin "os" qo‘shimcha emas
        ("pensiya", "пенсия"),
        ("versiya", "версия"),
        ("sexr", "сехр"),
    ],
)
def test_lugat_ortiqcha_ishlamaydi(lotin, krill):
    assert to_cyrillic(lotin) == krill


def test_yangi_lotindan_lugat():
    assert to_cyrillic("Şampun va kompyuter") == "Шампунь ва компьютер"


@pytest.mark.parametrize(
    "krill, lotin",
    [
        ("сентябрь", "sentabr"),
        ("Сентябрда", "Sentabrda"),
        ("октябрь", "oktabr"),
        ("ОКТЯБРЬ", "OKTABR"),
        ("обектив", "obyektiv"),
        ("Львов", "Livov"),
        ("бульон", "bulyon"),
        ("медальон", "medalyon"),
        ("сеньор", "senyor"),
    ],
)
def test_krilldan_lotinga(krill, lotin):
    assert to_latin(krill) == lotin
    assert to_new_latin(krill) == lotin


def test_lugat_kalitlari_toza():
    for kalit in list(LOTIN_KRILL) + list(KRILL_LOTIN) + list(KRILL_LOTIN.values()):
        assert kalit == kalit.lower()
        assert not set(kalit) & set("‘'`ʻʼ"), kalit
        assert "sh" not in kalit and "ch" not in kalit, f"{kalit}: ş/ç ishlating"


@pytest.mark.parametrize("lotin, krill", sorted(LOTIN_KRILL.items()))
def test_lugat_ikki_tomonlama(lotin, krill):
    # Lug‘atdagi har bir so‘z krilldan qaytganda ham o‘sha lotin shakliga tushadi
    assert to_cyrillic(lotin) == krill
    assert to_new_latin(krill) == lotin
