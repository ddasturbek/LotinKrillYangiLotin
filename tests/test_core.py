"""2-bosqich: yangi transliteratsiya yadrosi testlari."""

import pathlib
import unicodedata

import pytest

from LotinKrillYangiLotin import (
    OKINA,
    TUTUQ,
    detect_script,
    to_cyrillic,
    to_latin,
    to_new_latin,
)

F = {"krill": to_cyrillic, "lotin": to_latin, "yangi": to_new_latin}
DATA = pathlib.Path(__file__).resolve().parent.parent / "data"


# --- Murakkab holatlar (README va veb-demoda ham ko‘rsatiladi) ---------------

MURAKKAB_HOLATLAR = [
    ("krill", "ketsa aytsa", "кетса айтса"),
    ("krill", "Is’hoq", "Исҳоқ"),
    ("lotin", "Исҳоқ", "Is’hoq"),
    ("yangi", "Is’hoq", "Ishoq"),
    ("krill", "U ‘salom’ dedi", "У ‘салом’ деди"),
    ("krill", "(ertak)", "(эртак)"),
    ("lotin", "мебель", "mebel"),
    ("lotin", "ШАҲАР ва", "SHAHAR va"),
    ("lotin", "ПОЕЗД", "POYEZD"),
    ("yangi", "o‘zbek", "özbek"),
    ("krill", "Öğil", "Ўғил"),
]


@pytest.mark.parametrize("maqsad, kirish, kutilgan", MURAKKAB_HOLATLAR)
def test_murakkab_holatlar(maqsad, kirish, kutilgan):
    assert F[maqsad](kirish) == kutilgan


# --- Yangi alifbo (O‘RQ-1184) ------------------------------------------------

@pytest.mark.parametrize(
    "kirish, kutilgan",
    [
        ("o‘zbek", "özbek"),
        ("G‘ALABA", "ĞALABA"),
        ("ўғил", "öğil"),
        ("Чўл", "Çöl"),
        ("Шаҳар", "Şahar"),
        ("shamol choy", "şamol çoy"),
        ("SHAHAR CHOY", "ŞAHAR ÇOY"),
        ("O‘ZBEKISTON", "ÖZBEKISTON"),
        ("mo‘’tabar", "mö’tabar"),
        ("мўътабар", "mö’tabar"),
        ("ma’no", "ma’no"),
        ("Шу тизимни ўрганиш ва ишлатиш қобилиятига айтилади.",
         "Şu tizimni örganiş va işlatiş qobiliyatiga aytiladi."),
    ],
)
def test_yangi_lotinga(kirish, kutilgan):
    assert to_new_latin(kirish) == kutilgan


def test_yangi_harflar_unicode_kodlari():
    natija = to_new_latin("Ўў Ғғ Шш Чч")
    assert [hex(ord(c)) for c in natija if c != " "] == [
        "0xd6", "0xf6", "0x11e", "0x11f", "0x15e", "0x15f", "0xc7", "0xe7",
    ]
    assert unicodedata.is_normalized("NFC", natija)


def test_tutuq_belgisi_u2019():
    assert TUTUQ == "’"
    for kirish in ["ma'no", "ma`no", "maʼno", "maʻno", "ma’no", "маъно"]:
        assert to_new_latin(kirish) == "ma’no"
        assert to_latin(kirish) == "ma’no"


def test_eski_lotinda_okina_u2018():
    assert OKINA == "‘"
    assert to_latin("ўғил") == "o‘g‘il"


@pytest.mark.parametrize("kirish", ["ŞAHAR", "ȘAHAR", "ŞAHAR", "ȘAHAR"])
def test_s_harfi_variantlari(kirish):
    assert to_cyrillic(kirish) == "ШАҲАР"


def test_turkcha_klaviatura_i():
    assert to_new_latin("İkki qız") == "Ikki qiz"


def test_karonli_g():
    assert to_cyrillic("ǧalaba") == "ғалаба"


@pytest.mark.parametrize("kirish", ["Ō", "Ḡ"])
def test_eski_taklif_harflari_qollab_quvvatlanmaydi(kirish):
    # v1 dagi Ō/Ḡ endi alifboda yo‘q — o‘zgarishsiz qoladi
    assert to_cyrillic(kirish) == kirish


# --- Yangi lotindan boshqa yozuvlarga ----------------------------------------

@pytest.mark.parametrize(
    "kirish, lotin, krill",
    [
        ("Öğil", "O‘g‘il", "Ўғил"),
        ("Şahar çoy", "Shahar choy", "Шаҳар чой"),
        ("ÖZBEKISTON", "O‘ZBEKISTON", "ЎЗБЕКИСТОН"),
        ("Ishoq şoir", "Is’hoq shoir", "Исҳоқ шоир"),  # yangi lotinda sh = с+ҳ
        ("mö’tabar", "mo‘’tabar", "мўътабар"),
    ],
)
def test_yangi_lotindan(kirish, lotin, krill):
    assert to_latin(kirish) == lotin
    assert to_cyrillic(kirish) == krill


def test_manba_majburan_korsatish():
    # Ö/Ğ/Ş/Ç bo‘lmasa matn eski lotin deb olinadi: sh → ш
    assert to_cyrillic("Ishoq") == "Ишоқ"
    assert to_cyrillic("Ishoq", source="new_latin") == "Исҳоқ"
    with pytest.raises(ValueError):
        to_cyrillic("x", source="arab")


# --- Krill ↔ Lotin qoidalari --------------------------------------------------

@pytest.mark.parametrize(
    "krill, lotin",
    [
        ("поезд", "poyezd"),
        ("подъезд", "podyezd"),
        ("объектив", "obyektiv"),
        ("ер", "yer"),
        ("Ер", "Yer"),
        ("аэропорт", "aeroport"),
        ("элак", "elak"),
        ("функция", "funksiya"),
        ("акция", "aksiya"),
        ("милиция", "militsiya"),
        ("процент", "protsent"),
        ("рецепт", "retsept"),
        ("лицей", "litsey"),
        ("кетса", "ketsa"),
        ("айтса", "aytsa"),
        ("ёз", "yoz"),
        ("йўқ", "yo‘q"),
        ("Осиё", "Osiyo"),
        ("самолёт", "samolyot"),
        ("келяпти", "kelyapti"),
        ("боғ", "bog‘"),
        ("маъно", "ma’no"),
        ("пенсия", "pensiya"),
        ("цирк", "sirk"),
        ("Васильев", "Vasilyev"),
        ("пьеса", "pyesa"),
        ("коррупция", "korrupsiya"),
    ],
)
def test_krill_lotin_ikki_tomonlama(krill, lotin):
    assert to_latin(krill) == lotin
    assert to_cyrillic(lotin) == krill


@pytest.mark.parametrize(
    "krill, lotin",
    [
        ("Васильев", "Vasilyev"),
        ("съёмка", "syomka"),
        ("ЎЗБЕКИСТОН ЧОЙ Чой", "O‘ZBEKISTON CHOY Choy"),
        ("Ш", "Sh"),
        ("ТошДУ", "ToshDU"),
    ],
)
def test_krilldan_lotinga(krill, lotin):
    assert to_latin(krill) == lotin


# --- Himoyalangan qismlar va tinish belgilari ---------------------------------

def test_url_email_rim_raqamlari():
    kirish = "XX asr, IV bob. Sayt: https://kun.uz/news?id=1 pochta: test@mail.uz"
    assert to_cyrillic(kirish) == "XX аср, IV боб. Сайт: https://kun.uz/news?id=1 почта: test@mail.uz"


@pytest.mark.parametrize("matn", ["", "   ", "123 + 456 = 579", "—!?«»"])
def test_harfsiz_matn_ozgarmaydi(matn):
    for f in F.values():
        assert f(matn) == matn


def test_qoshtirnoqlar_va_tire():
    assert to_new_latin("«Ko‘p-ko‘p» – shunday") == "«Köp-köp» – şunday"
    assert to_cyrillic("U ‘yaxshi’ dedi") == "У ‘яхши’ деди"


def test_tur_xatosi():
    with pytest.raises(TypeError):
        to_latin(None)


# --- detect_script -------------------------------------------------------------

@pytest.mark.parametrize(
    "matn, yozuv",
    [
        ("Шаҳар", "cyrillic"),
        ("shahar o‘zbek", "latin"),
        ("şahar özbek", "new_latin"),
        ("123 !", "unknown"),
        ("Салом hello world", "mixed"),
        ("XX асрда яшаган олимлар", "cyrillic"),
    ],
)
def test_detect_script(matn, yozuv):
    assert detect_script(matn) == yozuv


# --- Korpus ("Til" maqolasi) -------------------------------------------------

@pytest.fixture(scope="module")
def korpus():
    return {
        k: (DATA / f"Til_{k}.txt").read_text(encoding="utf-8")
        for k in ("Krill", "Lotin", "YangiLotin")
    }


@pytest.mark.parametrize(
    "manba, maqsad",
    [
        ("Krill", "Lotin"), ("Krill", "YangiLotin"),
        ("Lotin", "Krill"), ("Lotin", "YangiLotin"),
        ("YangiLotin", "Krill"), ("YangiLotin", "Lotin"),
    ],
)
def test_korpus_belgima_belgi(korpus, manba, maqsad):
    f = {"Krill": to_cyrillic, "Lotin": to_latin, "YangiLotin": to_new_latin}[maqsad]
    assert f(korpus[manba]) == korpus[maqsad]


# --- Chidamlilik ---------------------------------------------------------------

@pytest.mark.parametrize("apostrof", ["ʻ", "ʼ", "'", "‘", "’", "`"])
def test_katta_harfli_soz_har_xil_apostrof(apostrof):
    assert to_new_latin(f"O{apostrof}ZBEKISTON") == "ÖZBEKISTON"
    assert to_latin(f"O{apostrof}ZBEKISTON") == "O‘ZBEKISTON"


@pytest.mark.parametrize("matn", ["ʻ", "/ʻ", "ʼʼʼ", "S»h .huʻ/ /./oÖoxg\ngʻubеa", "'", "o'", "''o"])
def test_faqat_apostroflar_osilib_qolmaydi(matn):
    for f in F.values():
        assert isinstance(f(matn), str)
    assert detect_script(matn) in {"cyrillic", "latin", "new_latin", "mixed", "unknown"}


def test_tasodifiy_matnlar():
    import random

    rnd = random.Random(2027)
    alifbo = "aboʻgʻ'’‘`shchSHÖğşçАЕЁЦЪЬъьеёюяцўғ -.,«»()\n1https://x.uz@OGog"
    for _ in range(3000):
        matn = "".join(rnd.choice(alifbo) for _ in range(rnd.randint(0, 40)))
        for f in F.values():
            assert isinstance(f(matn), str)


@pytest.mark.parametrize("f", [to_latin, to_cyrillic, to_new_latin])
def test_idempotent(korpus, f):
    for matn in korpus.values():
        bir = f(matn)
        assert f(bir) == bir
