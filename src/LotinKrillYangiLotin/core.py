"""
O‘zbek tili uchun Lotin ↔ Krill ↔ Yangi lotin transliteratsiya yadrosi.

Yangi lotin alifbosi: O‘RQ-1184-son Qonun (2026-yil 21-oktabr, kuchga kirishi
2027-yil 22-aprel). Unda O‘ → Ö, G‘ → Ğ, Sh → Ş, Ch → Ç; tutuq belgisi saqlanadi.

Ishlash tartibi
---------------
1. Matn normallashtiriladi (NFC, Ș → Ş, ı → i va hokazo).
2. URL va email manzillari himoyalanadi (o‘zgartirilmaydi).
3. Matn so‘zlarga bo‘linadi. Har bir so‘z yozuvdan qat’i nazar umumiy
   "fonema" ketma-ketligiga aylantiriladi (masalan, ``ў``, ``o‘``, ``ö`` → ``ö``).
4. Fonemalar maqsadli yozuvda qayta yoziladi. Registr har bir so‘z uchun
   alohida tiklanadi (``ШАҲАР`` → ``SHAHAR``, ``Шаҳар`` → ``Shahar``).
"""

from __future__ import annotations

import re
import unicodedata

from .lugat import KRILL_LOTIN, LOTIN_KRILL

__all__ = [
    "to_latin",
    "to_cyrillic",
    "to_new_latin",
    "detect_script",
    "TUTUQ",
    "OKINA",
]

#: Tutuq belgisi (U+2019 RIGHT SINGLE QUOTATION MARK) — barcha lotin chiqishlarida.
TUTUQ = "’"
#: Eski lotindagi O‘ va G‘ belgisi (U+2018 LEFT SINGLE QUOTATION MARK).
OKINA = "‘"

# Kirishda apostrof sifatida qabul qilinadigan barcha belgilar.
_APOSTROFLAR = frozenset("'`´ʹʻʼʽ‘’′")

_LAT_UNLILAR = frozenset("aeiouö")
_KR_UNLILAR = frozenset("аеёиоуўэюя")

# Kirishdagi turli variantlarni yagona shaklga keltirish.
_NORMALLASH = str.maketrans(
    {
        "Ș": "Ş", "ș": "ş",  # vergulli (rumincha) S → sedilli S
        "Ǧ": "Ğ", "ǧ": "ğ",  # karonli G → breveli G
        "ı": "i", "İ": "I",  # turkcha klaviatura nuqtasiz/nuqtali i
    }
)

_HIMOYA = re.compile(
    r"(?:https?://|www\.)\S+"           # URL
    r"|[\w.+-]+@[\w-]+(?:\.[\w-]+)+"    # email
)

_RIM = re.compile(r"M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})")

# --- Krill → fonema ---------------------------------------------------------

_KR_ODDIY = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "ж": "j", "з": "z",
    "и": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
    "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f", "х": "x",
    "ҳ": "h", "қ": "q", "ғ": "ğ", "ў": "ö", "ш": "ş", "ч": "ç", "э": "e",
    "ё": "yo", "ю": "yu", "я": "ya",
}

# --- Fonema → Krill ---------------------------------------------------------

_FON_KR = {
    "a": "а", "b": "б", "d": "д", "f": "ф", "g": "г", "ğ": "ғ", "h": "ҳ",
    "i": "и", "j": "ж", "k": "к", "l": "л", "m": "м", "n": "н", "o": "о",
    "ö": "ў", "p": "п", "q": "қ", "r": "р", "s": "с", "ş": "ш", "ç": "ч",
    "t": "т", "u": "у", "v": "в", "x": "х", "y": "й", "z": "з", TUTUQ: "ъ",
}
_Y_BIRIKMA = {"o": "ё", "u": "ю", "a": "я"}

# "ts" faqat shu qoliplarda (unlidan keyin) ц bo‘ladi: militsiya, stansiya emas,
# protsent, retsept, litsey, mototsikl. Qolgan hollarda т+с: ketsa, aytsa.
_TS_QOLIPLAR = ("iya", "io", "ent", "ept", "enz", "ikl", "ey")

# --- Fonema → lotin ---------------------------------------------------------

_FON_YANGI = {TUTUQ: TUTUQ}
_FON_ESKI = {"ö": "o" + OKINA, "ğ": "g" + OKINA, "ş": "sh", "ç": "ch", TUTUQ: TUTUQ}


class _Fon:
    """Bitta fonema: ``ph`` — lotincha qiymat, ``katta`` — bosh harfmi,
    ``kr`` — agar manba krillcha bo‘lsa, asl krill belgisi (o‘zgarishsiz qaytarish uchun),
    ``xom`` — tanilmagan belgi bo‘lsa, o‘zi."""

    __slots__ = ("ph", "katta", "kr", "xom")

    def __init__(self, ph, katta, kr=None, xom=None):
        self.ph = ph
        self.katta = katta
        self.kr = kr
        self.xom = xom


def _registr(s: str, katta: bool, hammasi_katta: bool) -> str:
    if not katta:
        return s
    if hammasi_katta:
        return s.upper()
    return s[:1].upper() + s[1:]


def _harf(c: str) -> bool:
    """Harfmi? ʻ va ʼ Unicode’da "harf" (Lm) hisoblanadi, lekin biz uchun apostrof."""
    return c.isalpha() and c not in _APOSTROFLAR


def _hammasi_katta(soz: str) -> bool:
    harflar = [c for c in soz if _harf(c)]
    return len(harflar) >= 2 and all(c.isupper() for c in harflar)


def _is_kr(c: str) -> bool:
    return "Ѐ" <= c <= "ӿ"


# --- So‘zni fonemalarga ajratish --------------------------------------------

def _tahlil(soz: str, yangi_lotin: bool) -> tuple[list[list[_Fon]], bool]:
    """So‘zni fonema guruhlariga ajratadi. Har bir guruh — bitta manba belgisiga mos."""
    hk = _hammasi_katta(soz)
    guruhlar: list[list[_Fon]] = []
    n = len(soz)
    i = 0
    while i < n:
        c = soz[i]
        lc = c.lower()
        katta = c.isupper()
        nxt = soz[i + 1] if i + 1 < n else ""

        if _is_kr(c):
            oldingi = soz[i - 1].lower() if i > 0 else ""
            if lc == "е":
                boshida = i == 0 or oldingi in _KR_UNLILAR or oldingi in _LAT_UNLILAR or oldingi in "ъь"
                if boshida:
                    guruhlar.append([_Fon("y", katta, c), _Fon("e", katta and hk, "")])
                else:
                    guruhlar.append([_Fon("e", katta, c)])
            elif lc in "ёюя":
                ph = _KR_ODDIY[lc]
                guruhlar.append([_Fon(ph[0], katta, c), _Fon(ph[1], katta and hk, "")])
            elif lc == "ц":
                if oldingi and (oldingi in _KR_UNLILAR or oldingi in _LAT_UNLILAR):
                    guruhlar.append([_Fon("t", katta, c), _Fon("s", katta and hk, "")])
                else:
                    guruhlar.append([_Fon("s", katta, c)])
            elif lc == "ъ":
                if nxt.lower() in ("е", "ё", "ю", "я"):
                    guruhlar.append([_Fon("", katta, c)])  # подъезд → podyezd
                else:
                    guruhlar.append([_Fon(TUTUQ, hk, c)])
            elif lc == "ь":
                if nxt.lower() == "о":
                    guruhlar.append([_Fon("y", katta and hk, c)])  # бульон → bulyon
                else:
                    guruhlar.append([_Fon("", katta, c)])  # мебель → mebel
            elif lc in _KR_ODDIY:
                guruhlar.append([_Fon(_KR_ODDIY[lc], katta, c)])
            else:
                guruhlar.append([_Fon("", katta, c, xom=c)])
            i += 1
            continue

        if c in _APOSTROFLAR:
            guruhlar.append([_Fon(TUTUQ, hk)])
            i += 1
            continue

        # Lotin harflari
        if lc in "og" and nxt in _APOSTROFLAR:
            guruhlar.append([_Fon("ö" if lc == "o" else "ğ", katta)])
            i += 2
            continue
        if lc in "sc" and nxt in _APOSTROFLAR and i + 2 < n and soz[i + 2].lower() == "h":
            # s’h (Is’hoq) — ajratuvchi apostrof, tutuq emas
            guruhlar.append([_Fon(lc, katta)])
            guruhlar.append([_Fon("h", soz[i + 2].isupper())])
            i += 3
            continue
        if not yangi_lotin and lc in "sc" and nxt.lower() == "h":
            guruhlar.append([_Fon("ş" if lc == "s" else "ç", katta)])
            i += 2
            continue
        if lc in "öğşç" or ("a" <= lc <= "z" and lc not in "cw"):
            guruhlar.append([_Fon(lc, katta)])
        else:
            guruhlar.append([_Fon("", katta, xom=c)])
        i += 1
    return guruhlar, hk


# --- Fonemalardan yozish ----------------------------------------------------

def _lotinga_yoz(guruhlar, hk, yangi: bool) -> str:
    fon = [f for g in guruhlar for f in g]
    jadval = _FON_YANGI if yangi else _FON_ESKI
    natija = []
    for j, f in enumerate(fon):
        if f.xom is not None:
            natija.append(f.xom)
            continue
        if not f.ph:
            continue
        s = jadval.get(f.ph, f.ph)
        if not yangi and f.ph == "s" and j + 1 < len(fon) and fon[j + 1].ph == "h":
            s = "s" + TUTUQ  # сҳ / Ishoq → Is’hoq (eski lotinda sh = ш bo‘lgani uchun)
        natija.append(_registr(s, f.katta, hk))
    return "".join(natija)


def _ts_ts(fon, j) -> bool:
    """fon[j] == 't', fon[j+1] == 's': ц bo‘lishi kerakmi?"""
    if j == 0 or fon[j - 1].ph not in _LAT_UNLILAR:
        return False
    keyin = "".join(f.ph for f in fon[j + 2: j + 6])
    return any(keyin.startswith(q) for q in _TS_QOLIPLAR)


def _krillga_yoz(guruhlar, hk, oldingi: str = "") -> str:
    fon = [f for g in guruhlar for f in g]
    natija = []
    j = 0
    n = len(fon)
    while j < n:
        f = fon[j]
        if f.kr is not None:  # manba krillcha — o‘zgarishsiz
            natija.append(f.kr)
            if f.ph:
                oldingi = f.ph
            j += 1
            continue
        if f.xom is not None:
            natija.append(f.xom)
            oldingi = "?"  # tanilmagan harf undosh deb olinadi (Wernicke → Wерниcке)
            j += 1
            continue
        ph = f.ph
        keyingi = fon[j + 1] if j + 1 < n and fon[j + 1].kr is None and fon[j + 1].xom is None else None
        k = keyingi.ph if keyingi else ""

        if ph == "y" and k == "e":
            # undoshdan keyin: obyekt → объект, podyezd → подъезд (old qo‘shimcha
            # undoshlari b, d, s, z), qolganlarida ь: Vasilyev → Васильев, pyesa → пьеса
            if oldingi and oldingi not in _LAT_UNLILAR and oldingi != TUTUQ:
                belgi = "ъ" if oldingi in ("b", "d", "s", "z") else "ь"
                natija.append(_registr(belgi + "е", hk, hk))
            else:
                natija.append(_registr("е", f.katta, hk))
            oldingi = "e"
            j += 2
            continue
        if ph == "y" and k in _Y_BIRIKMA:
            natija.append(_registr(_Y_BIRIKMA[k], f.katta, hk))
            oldingi = k
            j += 2
            continue
        if ph == "t" and k == "s" and _ts_ts(fon, j):
            natija.append(_registr("ц", f.katta, hk))
            oldingi = "s"
            j += 2
            continue
        if ph == "s" and oldingi in ("k", "p") and "".join(x.ph for x in fon[j + 1: j + 4]) == "iya":
            natija.append(_registr("ц", f.katta, hk))  # funksiya → функция, korrupsiya → коррупция
            oldingi = "s"
            j += 1
            continue
        if ph == "e":
            boshida = not oldingi or oldingi in _LAT_UNLILAR
            natija.append(_registr("э" if boshida else "е", f.katta, hk))
            oldingi = "e"
            j += 1
            continue
        s = _FON_KR.get(ph, ph)
        natija.append(_registr(s, f.katta, hk))
        oldingi = ph
        j += 1
    return "".join(natija)


# --- Matnni so‘zlarga bo‘lish -----------------------------------------------

# --- Istisnolar lug‘ati -------------------------------------------------------

# O‘zakdan keyin keladigan qo‘shimchalar zanjiri (yangi lotin fonemalarida).
_QOSHIMCHA = re.compile(
    r"(?:lar)?"
    r"(?:im|ing|i|si|imiz|ingiz|miz|ngiz|m|ng)?"
    r"(?:ni|ning|ga|ka|qa|da|ta|dan|tan|dagi|day|dek|ça|çi|lik|li|siz)?"
    r"(?:mi|ku|u|yu|gina)?"
)
_LK_KALITLAR = sorted(LOTIN_KRILL, key=len, reverse=True)
_KL_KALITLAR = sorted(KRILL_LOTIN, key=len, reverse=True)


def _lugat_krillga(guruhlar, hk) -> str | None:
    """Lotin so‘zi LOTIN_KRILL lug‘atidagi o‘zak bilan boshlansa, krillcha yozadi."""
    fon = [f for g in guruhlar for f in g]
    if not fon or any(f.kr is not None or f.xom is not None or len(f.ph) != 1 for f in fon):
        return None
    kalit = "".join(f.ph for f in fon).lower()
    for ozak in _LK_KALITLAR:
        if kalit.startswith(ozak) and _QOSHIMCHA.fullmatch(kalit[len(ozak):]):
            kr = LOTIN_KRILL[ozak]
            qolgan = fon[len(ozak):]
            if qolgan and kr.endswith("ь"):
                kr = kr[:-1]  # sentabrda → сентябрда
            kr = _registr(kr, fon[0].katta, hk)
            return kr + _krillga_yoz([qolgan], hk, oldingi=ozak[-1])
    return None


def _lugat_lotinga(guruhlar, hk):
    """Krill so‘zidan chiqqan fonemalarni KRILL_LOTIN bo‘yicha to‘g‘rilaydi."""
    fon = [f for g in guruhlar for f in g]
    if not fon or not all(f.kr is not None and f.xom is None for f in fon):
        return guruhlar
    tekis = [f for f in fon if f.ph]
    kalit = "".join(f.ph for f in tekis)
    if any(len(f.ph) != 1 for f in tekis):
        return guruhlar
    for xato in _KL_KALITLAR:
        if kalit.startswith(xato):
            togri = KRILL_LOTIN[xato]
            yangi = [_Fon(c, tekis[0].katta if k == 0 else hk and tekis[0].katta, "")
                     for k, c in enumerate(togri)]
            return [yangi + tekis[len(xato):]]
    return guruhlar


def _normallash(matn: str) -> str:
    return unicodedata.normalize("NFC", matn).translate(_NORMALLASH)


def _qismlar(matn: str):
    """(is_soz, bo‘lak) juftliklarini qaytaradi. URL/email himoyalangan (is_soz=False)."""
    pos = 0
    for m in _HIMOYA.finditer(matn):
        yield from _sozlar(matn[pos:m.start()])
        yield False, m.group()
        pos = m.end()
    yield from _sozlar(matn[pos:])


def _sozlar(matn: str):
    n = len(matn)
    i = 0
    boshi = 0
    while i < n:
        if not _harf(matn[i]):
            i += 1
            continue
        if boshi < i:
            yield False, matn[boshi:i]
        j = i
        while j < n:
            c = matn[j]
            if _harf(c):
                j += 1
            elif c in _APOSTROFLAR:
                keyin = matn[j + 1] if j + 1 < n else ""
                oldin = matn[j - 1]
                # so‘z ichidagi apostrof yoki o‘/g‘ (bog‘, tog‘)
                if _harf(keyin) or keyin in _APOSTROFLAR or oldin in "oOgG":
                    j += 1
                else:
                    break
            else:
                break
        # so‘z oxiridagi ortiqcha apostroflarni qaytarib qo‘yish (o/g dan keyingisidan tashqari)
        while j > i and matn[j - 1] in _APOSTROFLAR and matn[j - 2] not in "oOgG":
            j -= 1
        j = max(j, i + 1)  # har doim oldinga siljish kafolati
        yield True, matn[i:j]
        i = boshi = j
    if boshi < n:
        yield False, matn[boshi:]


def _yangi_lotinmi(matn: str, manba: str | None) -> bool:
    if manba is not None:
        if manba not in ("latin", "new_latin", "cyrillic"):
            raise ValueError("manba quyidagilardan biri bo‘lishi kerak: 'latin', 'new_latin', 'cyrillic'")
        return manba == "new_latin"
    return any(c in "ÖöĞğŞşÇç" for c in matn)


def _almashtir(matn: str, maqsad: str, manba: str | None) -> str:
    if not isinstance(matn, str):
        raise TypeError("matn str bo‘lishi kerak")
    matn = _normallash(matn)
    yangi = _yangi_lotinmi(matn, manba)
    natija = []
    for soz_mi, bolak in _qismlar(matn):
        if not soz_mi:
            natija.append(bolak)
            continue
        if maqsad == "cyrillic" and not any(_is_kr(c) for c in bolak) and _RIM.fullmatch(bolak):
            natija.append(bolak)  # XX asr, IV bob
            continue
        guruhlar, hk = _tahlil(bolak, yangi)
        if maqsad == "cyrillic":
            natija.append(_lugat_krillga(guruhlar, hk) or _krillga_yoz(guruhlar, hk))
        else:
            guruhlar = _lugat_lotinga(guruhlar, hk)
            natija.append(_lotinga_yoz(guruhlar, hk, yangi=(maqsad == "new_latin")))
    return "".join(natija)


# --- Ommaviy API ------------------------------------------------------------

def to_latin(text: str, source: str | None = None) -> str:
    """Matnni amaldagi (1995) o‘zbek lotin yozuviga o‘tkazadi.

    ``O‘ G‘`` uchun ``‘`` (U+2018), tutuq belgisi uchun ``’`` (U+2019) ishlatiladi.

    :param text: krill, lotin yoki yangi lotin (yoki aralash) matn
    :param source: lotin matn qaysi variantda ekanini majburan ko‘rsatish:
        ``"latin"`` yoki ``"new_latin"``. Ko‘rsatilmasa avtomatik aniqlanadi.
    """
    return _almashtir(text, "latin", source)


def to_new_latin(text: str, source: str | None = None) -> str:
    """Matnni yangi o‘zbek lotin yozuviga (O‘RQ-1184, 2027) o‘tkazadi: Ö Ğ Ş Ç, tutuq ``’``."""
    return _almashtir(text, "new_latin", source)


def to_cyrillic(text: str, source: str | None = None) -> str:
    """Matnni o‘zbek krill yozuviga o‘tkazadi."""
    return _almashtir(text, "cyrillic", source)


def detect_script(text: str) -> str:
    """Matn yozuvini aniqlaydi.

    :return: ``"cyrillic"``, ``"latin"``, ``"new_latin"``, ``"mixed"`` yoki ``"unknown"``.
    """
    matn = _normallash(text)
    kr = lat = 0
    for soz_mi, soz in _sozlar(matn):
        if not soz_mi or _RIM.fullmatch(soz):  # rim raqamlari hisobga olinmaydi
            continue
        for c in soz:
            if _is_kr(c):
                kr += 1
            elif c.lower() in "abcdefghijklmnopqrstuvwxyzöğşç":
                lat += 1
    jami = kr + lat
    if jami == 0:
        return "unknown"
    if kr and lat and min(kr, lat) / jami >= 0.1:
        return "mixed"
    if kr > lat:
        return "cyrillic"
    return "new_latin" if _yangi_lotinmi(matn, None) else "latin"
