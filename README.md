# LotinKrillYangiLotin

[![Testlar](https://github.com/ddasturbek/LotinKrillYangiLotin/actions/workflows/tests.yml/badge.svg)](https://github.com/ddasturbek/LotinKrillYangiLotin/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/LotinKrillYangiLotin)](https://pypi.org/project/LotinKrillYangiLotin/)
[![Python](https://img.shields.io/pypi/pyversions/LotinKrillYangiLotin)](https://pypi.org/project/LotinKrillYangiLotin/)
[![Litsenziya: MIT](https://img.shields.io/badge/litsenziya-MIT-blue)](https://github.com/ddasturbek/LotinKrillYangiLotin/blob/main/LICENSE)

O‘zbek tilidagi matnlarni **Lotin**, **Krill** va **Yangi lotin** yozuvlari o‘rtasida almashtiruvchi Python kutubxonasi va terminal buyrug‘i.

**Muallif:** [Dasturbek](https://github.com/ddasturbek)

**Veb-demo:** [ddasturbek.github.io/LotinKrillYangiLotin](https://ddasturbek.github.io/LotinKrillYangiLotin/) — o‘rnatmasdan brauzerda sinab ko‘ring.

## Yangi alifbo haqida

2026-yil 21-oktabrda imzolangan [O‘RQ-1184-son Qonun](https://www.lex.uz/uz/docs/8548754) bilan lotin yozuviga asoslangan o‘zbek alifbosi takomillashtirildi. Qonun **2027-yil 22-apreldan** kuchga kiradi. Alifbo 26 harf va 3 harf birikmasi o‘rniga **28 harf va bitta tutuq belgisidan** iborat bo‘ladi:

| Krill | Amaldagi lotin (1995) | Yangi lotin (2027) | Misol |
|:-:|:-:|:-:|---|
| Ў ў | O‘ o‘ | **Ö ö** | ўқитувчи → o‘qituvchi → **ö**qituvçi |
| Ғ ғ | G‘ g‘ | **Ğ ğ** | ғалаба → g‘alaba → **ğ**alaba |
| Ш ш | Sh sh | **Ş ş** | шаҳар → shahar → **ş**ahar |
| Ч ч | Ch ch | **Ç ç** | чой → choy → **ç**oy |
| Ъ ъ | ’ | **’** | маъно → ma’no → ma’no |

“Ng” birikmasi alohida harf sifatida alifbodan chiqarildi (yozilishi o‘zgarmaydi). Batafsil: [alfavit.uz](https://alfavit.uz/alphabet).

Kutubxona chiqishida quyidagi belgilar ishlatiladi:

| Belgi | Unicode | Qayerda |
|:-:|:-:|---|
| `Ö ö` `Ğ ğ` `Ş ş` `Ç ç` | U+00D6/F6, U+011E/1F, U+015E/5F, U+00C7/E7 | yangi lotin |
| `’` | U+2019 | tutuq belgisi (ikkala lotin yozuvida) |
| `‘` | U+2018 | amaldagi lotindagi `O‘ G‘` |

Kirishda esa barcha keng tarqalgan variantlar qabul qilinadi: `o'`, `` o` ``, `oʻ`, `oʼ`, `o’`, rumincha `Ș`, turkcha klaviaturadagi `ı`/`İ` va boshqalar.

## O‘rnatish

```bash
pip install LotinKrillYangiLotin
```

Python 3.10 yoki undan yangi versiya kerak. Kutubxonaning boshqa bog‘liqliklari yo‘q.

## Foydalanish

```python
from LotinKrillYangiLotin import to_latin, to_cyrillic, to_new_latin, detect_script

to_new_latin("Шу тизимни ўрганиш ва ишлатиш қобилиятига айтилади.")
# 'Şu tizimni örganiş va işlatiş qobiliyatiga aytiladi.'

to_new_latin("O‘zbekiston choy")   # 'Özbekiston çoy'
to_latin("Öğil şahar")            # 'O‘g‘il shahar'
to_cyrillic("Öğil şahar")         # 'Ўғил шаҳар'
to_cyrillic("geometriya")         # 'геометрия'
to_latin("функция")               # 'funksiya'

detect_script("Шаҳар")            # 'cyrillic'
detect_script("shahar")           # 'latin'
detect_script("şahar")            # 'new_latin'
```

Kirish matni istalgan yozuvda (hatto aralash) bo‘lishi mumkin: har bir funksiya manbani o‘zi aniqlaydi.

| Funksiya | Natija |
|---|---|
| `to_latin(text)` | amaldagi lotin (1995) |
| `to_cyrillic(text)` | krill |
| `to_new_latin(text)` | yangi lotin (2027) |
| `detect_script(text)` | `"cyrillic"`, `"latin"`, `"new_latin"`, `"mixed"` yoki `"unknown"` |

### `source` parametri

Matnda `Ö Ğ Ş Ç` harflaridan birortasi ham bo‘lmasa, uni yangi lotinda yozilgan deb aniqlab bo‘lmaydi. Shunda matn amaldagi lotin deb olinadi va `sh` → `ш` bo‘ladi. Yangi lotin ekanini aniq bilsangiz, `source` bilan ko‘rsating:

```python
to_cyrillic("Ishoq")                       # 'Ишоқ'  (sh = ш deb olindi)
to_cyrillic("Ishoq", source="new_latin")   # 'Исҳоқ' (yangi lotinda sh = с+ҳ)
```

## Terminal buyrug‘i

O‘rnatilgandan so‘ng `lky` buyrug‘i paydo bo‘ladi (yoki `python -m LotinKrillYangiLotin`):

```bash
lky -t yangi kitob.txt -o kitob_yangi.txt   # faylni yangi lotinga
lky -t krill -m "O‘zbekiston"               # Ўзбекистон
echo "Шаҳар" | lky -t yangi                 # Şahar
lky --aniqlash kitob.txt                    # cyrillic
lky -t krill -s yangi -m "Ishoq"            # Исҳоқ
```

| Parametr | Ma’nosi |
|---|---|
| `-t`, `--to` | maqsad yozuv: `lotin`, `krill`, `yangi` |
| `-m`, `--matn` | faylsiz, to‘g‘ridan-to‘g‘ri matn |
| `-o`, `--chiqish` | natijani faylga yozish |
| `-s`, `--manba` | lotin matn variantini majburan ko‘rsatish: `lotin` yoki `yangi` |
| `-a`, `--aniqlash` | faqat yozuvni aniqlash |

## Murakkab holatlar

Oddiy “harfni harfga almashtirish” bilan to‘g‘ri chiqmaydigan holatlar. Jadvaldagi har bir qator avtomatik testlar bilan tekshiriladi (`tests/test_readme.py`), ya’ni dastur aynan shu natijani beradi.

<!-- murakkab-holatlar:boshi -->
| Kirish | Yo‘nalish | Natija | Nima uchun murakkab |
|---|---|---|---|
| `ketsa aytsa` | Krill | `кетса айтса` | `ts` har doim `ц` emas: bu yerda т+с |
| `Is’hoq` | Krill | `Исҳоқ` | `s’h` — ajratuvchi, tutuq (ъ) emas |
| `Исҳоқ` | Lotin | `Is’hoq` | amaldagi lotinda `sh` = ш bo‘lgani uchun `s’h` |
| `Is’hoq` | Yangi lotin | `Ishoq` | yangi lotinda `ş` bor, ajratish shart emas |
| `U ‘salom’ dedi` | Krill | `У ‘салом’ деди` | qo‘shtirnoq tutuq belgisidan farqlanadi |
| `(ertak)` | Krill | `(эртак)` | qavsdan keyin ham so‘z boshi: `э` |
| `мебель` | Lotin | `mebel` | `ь` tushiriladi |
| `mebel` | Krill | `мебель` | `ь` lug‘at orqali tiklanadi |
| `ШАҲАР ва` | Lotin | `SHAHAR va` | registr har bir so‘z uchun alohida |
| `ПОЕЗД` | Lotin | `POYEZD` | unlidan keyingi `е` → `ye` |
| `obyektiv` | Krill | `объектив` | undoshdan keyingi `ye` → `ъе` |
| `o‘zbek` | Yangi lotin | `özbek` | `o‘` → `ö` |
| `Öğil` | Krill | `Ўғил` | yangi lotin harflari to‘g‘ridan-to‘g‘ri |
| `mo‘’tabar` | Yangi lotin | `mö’tabar` | `o‘` va tutuq belgisi yonma-yon |
| `funksiya, militsiya` | Krill | `функция, милиция` | `-ksiya` → `кция`, `-tsiya` → `ция` |
| `15-sentabrda` | Krill | `15-сентябрда` | qo‘shimcha bilan `ь` tushadi |
| `Сентябрь` | Yangi lotin | `Sentabr` | o‘zbek imlosi: `sentabr` |
| `XX asr, https://kun.uz` | Krill | `XX аср, https://kun.uz` | rim raqamlari va URL o‘zgarmaydi |
<!-- murakkab-holatlar:oxiri -->

## Qoidalar

Asosiy manba — [O‘zbek tilining asosiy imlo qoidalari](https://lex.uz/docs/1625271) (Vazirlar Mahkamasining 1995-yil 24-avgustdagi 339-son qarori).

**Е / Э**
- Krill `е` so‘z boshida, unlidan, `ъ` yoki `ь` dan keyin `ye` bo‘ladi (`егулик` → `yegulik`, `поезд` → `poyezd`, `подъезд` → `podyezd`, `Васильев` → `Vasilyev`), qolgan hollarda `e`.
- Lotin `e` so‘z boshida va unlidan keyin `э` (`elak` → `элак`, `aeroport` → `аэропорт`), undoshdan keyin `е`.
- Lotin `ye` → `е`; undoshdan keyin `b d s z` bo‘lsa `ъе` (`obyekt` → `объект`), boshqa undoshdan keyin `ье` (`pyesa` → `пьеса`).

**Ц**
- Krill `ц` unlidan keyin `ts`, qolgan hollarda `s` (`милиция` → `militsiya`, `функция` → `funksiya`, `цирк` → `sirk`).
- Lotin `ts` faqat o‘zlashma qoliplarda `ц` (`-tsiya`, `-tsent`, `-tsept`, `litsey` ...), aks holda `тс` (`ketsa` → `кетса`). `-ksiya`, `-psiya` → `-кция`, `-пция`.

**Ъ / Ь**
- `ъ` → tutuq `’` (`маъно` → `ma’no`); `е ё ю я` oldidan tushiriladi.
- `ь` tushiriladi (`мебель` → `mebel`); `ьо` → `yo` (`бульон` → `bulyon`).

**Ё Ю Я** → `yo yu ya`, teskarisi ham.

### Istisnolar lug‘ati

Qoida bilan tiklab bo‘lmaydigan so‘zlar ([`lugat.py`](https://github.com/ddasturbek/LotinKrillYangiLotin/blob/main/src/LotinKrillYangiLotin/lugat.py)) — masalan `sirk` → `цирк`, `kompyuter` → `компьютер`, `сентябрь` → `sentabr`. Lug‘atdagi so‘zlar o‘zbekcha qo‘shimchalar bilan ham taniladi (`sirkda` → `циркда`), lekin tasodifiy o‘xshash so‘zlar o‘zgarmaydi (`sirka` → `сирка`).

Yangi so‘z qo‘shmoqchi bo‘lsangiz, `lugat.py` ga qator va `tests/test_lugat.py` ga misol qo‘shib, Pull Request yuboring.

## 1.x versiyadan o‘tish

2.0.0 versiyada yangi lotin harflari qonunga moslashtirildi va API yangilandi.

| 1.x | 2.x |
|---|---|
| `Almashtirish().Lotinga(t)` | `to_latin(t)` |
| `Almashtirish().Krillga(t)` | `to_cyrillic(t)` |
| `Almashtirish().YangiLotinga(t)` | `to_new_latin(t)` |
| yangi lotin: `Ō ō Ḡ ḡ` | `Ö ö Ğ ğ` |
| tutuq: `ʼ` (U+02BC) | `’` (U+2019) |

`Almashtirish` klassi hamon ishlaydi, lekin `DeprecationWarning` beradi va 3.0.0 versiyada olib tashlanadi. Barcha o‘zgarishlar: [CHANGELOG.md](https://github.com/ddasturbek/LotinKrillYangiLotin/blob/main/CHANGELOG.md).

## Ishlab chiqish

```bash
git clone https://github.com/ddasturbek/LotinKrillYangiLotin.git
cd LotinKrillYangiLotin
pip install -e ".[dev]"
pytest
```

Veb-demoni lokal ko‘rish:

```bash
python docs/build.py && python -m http.server -d _site
```

Demo (`docs/index.html`) brauzerda [Pyodide](https://pyodide.org/) orqali `src/` dagi kutubxonaning aynan o‘zini ishga tushiradi, misollar esa README’dagi “Murakkab holatlar” jadvalidan olinadi. `main` ga har bir push’dan keyin GitHub Pages’ga avtomatik joylanadi.

`data/` papkasida Vikipediyadagi “Til” maqolasi uch yozuvda saqlangan. Testlar ular o‘rtasidagi barcha 6 yo‘nalishda natija belgima-belgi mos kelishini tekshiradi.

## Litsenziya

[MIT](https://github.com/ddasturbek/LotinKrillYangiLotin/blob/main/LICENSE)
