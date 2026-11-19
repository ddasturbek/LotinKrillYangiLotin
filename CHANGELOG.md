# O‘zgarishlar tarixi

Format [Keep a Changelog](https://keepachangelog.com/) ga, versiyalash [SemVer](https://semver.org/) ga asoslangan.

## [2.0.0] — 2026-11-19

Yangi o‘zbek lotin alifbosiga ([O‘RQ-1184-son Qonun](https://www.lex.uz/uz/docs/8548754), 2027-yil 22-apreldan kuchga kiradi) to‘liq moslashtirildi. Transliteratsiya yadrosi qaytadan yozildi.

### Ta’sirli o‘zgarishlar
- Yangi lotin harflari qonunga moslashtirildi: `Ō ō` → **`Ö ö`**, `Ḡ ḡ` → **`Ğ ğ`** (`Ş ş`, `Ç ç` o‘zgarmadi).
- Tutuq belgisi barcha lotin chiqishlarida `’` (U+2019).
- `Ō`, `Ḡ` endi kirishda ham tanilmaydi.
- Python ≥ 3.10 talab qilinadi.

### Qo‘shildi
- Yangi API: `to_latin()`, `to_cyrillic()`, `to_new_latin()`, `detect_script()`, `TUTUQ`, `OKINA`.
- `source=` parametri — lotin matn variantini majburan ko‘rsatish.
- `lky` terminal buyrug‘i va `python -m LotinKrillYangiLotin`.
- Veb-demo (GitHub Pages + Pyodide): kutubxonaning o‘zi brauzerda ishlaydi.
- Istisnolar lug‘ati (`lugat.py`): `ь`, `ц`, `э` bilan yoziladigan o‘zlashmalar, oylar; o‘zbekcha qo‘shimchalar bilan ham ishlaydi.
- Kirishni normallashtirish: Unicode NFC, `Ș` → `Ş`, `ǧ` → `ğ`, `ı`/`İ` → `i`/`I`, barcha apostrof variantlari.
- URL, email va rim raqamlari o‘zgartirilmaydi.
- 250 dan ortiq test, GitHub Actions CI (Python 3.10–3.14), README misollari avtomatik tekshiriladi.

### Tuzatildi
- `ketsa`, `aytsa` → `кетса`, `айтса` (avval `кеца`, `айца`).
- `Is’hoq` ↔ `Исҳоқ` ↔ yangi lotinda `Ishoq` (avval `Исъҳоқ`, `Ishoq`, `Is’hoq`).
- Qo‘shtirnoqlar `ъ` ga aylanib ketmaydi.
- Qavs, tire va boshqa belgilardan keyingi `e` → `э`.
- Krill `ь` lotinga o‘tmay qolardi (`mebelь`).
- Registr butun matn bo‘yicha emas, har bir so‘z uchun aniqlanadi (`ШАҲАР ва` → `SHAHAR va`, `ПОЕЗД` → `POYEZD`).
- Krill unlilar ro‘yxatida lotincha `E` xatosi.
- `обектив` → `obyektiv`.

### Eskirdi
- `Almashtirish` klassi (`Lotinga`, `Krillga`, `YangiLotinga`) — `DeprecationWarning` beradi, 3.0.0 da olib tashlanadi.

## [1.0.0] — 2024

- Birinchi versiya: `Almashtirish` klassi, Fanlar akademiyasi taklif etgan yangi lotin varianti (`Ō Ḡ Ş Ç`).

[2.0.0]: https://github.com/ddasturbek/LotinKrillYangiLotin/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ddasturbek/LotinKrillYangiLotin/releases/tag/v1.0.0
