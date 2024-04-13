## Dastur haqida
**Muallif: [Dasturbek](https://github.com/ddasturbek)**
**Dastur nomi:** LotinKrillYangilotin
**Versiya: 1.0.0**
**Dastur tili:** Python

Dasturdan o‘zbek tilidagi matnlarni yozuv shaklini almashtirishda va yangi lotin alifbosini joriy qilishda foydalanish mumkin!

## Dasturni o‘rnatish

Siz dasturni Python loyihangizga [pip](https://pypi.org/project/LotinKrillYangiLotin) orqali o‘rnatib foydalanishingiz mumkin.

```bash
pip install LotinKrillYangiLotin
```

Yoki [Githubdan](https://github.com/ddasturbek/LotinKrillYangiLotin) klonlab foydalanishingiz mumkin.

```bash
git clone https://github.com/ddasturbek/LotinKrillYangiLotin.git
```

## Dasturdan foydalanish

```Python
from LotinKrillYangiLotin import Almashtirish
# Obyekt yaratish
almashtir = Almashtirish()

print(almashtir.Lotinga('функция'))  # funksiya
print(almashtir.Krillga('geometriya'))  # геометрия
print(almashtir.YangiLotinga('shamol'))  # şamol
```

Funksiyalar faqat so‘zlarni emas balki matnlar shaklini ham almashtira oladi.

Birorta shaklga o‘tkazganda qolgan shakllarni o‘zi tanib oladi.

Ya’ni YangiLotinga funksiyasiga Lotincha yoki Krillcha matnlarni kiritsa bo‘ladi va aksincha.

```Python
print(almashtir.YangiLotinga("Shu tizimni o‘rganish va ishlatish qobiliyatiga aytiladi."))  # Şu tizimni ōrganiş va işlatiş qobiliyatiga aytiladi.
print(almashtir.YangiLotinga("Шу тизимни ўрганиш ва ишлатиш қобилиятига айтилади."))  # Şu tizimni ōrganiş va işlatiş qobiliyatiga aytiladi.
```

## Alifbo haqida

Yangi lotin yozuvi haqida [taklif](https://regulation.gov.uz/oz/d/31596) O‘zbekiston Respublikasi Fanlar akademiyasi tomonidan 'NORMATIV-HUQUQIY HUJJATLAR LOYIHALARI MUHOKAMASI PORTALI'ga muhokamaga qo‘yilgan.

* O‘zbek Lotin alifbosida 29 harf va bitta tutuq belgi (’) bor.
* O‘zbek Krill alifbosida shunga mos, ya’ni 30 ta harf va belgi bor.
* O‘zbek Yangi lotin alifbosida ham jami 30 ta harf va belgi bor.

Alifbo bilan to‘liq holda quyida tanishishingiz mumkin.

![LotinKrillYangiLotin](https://github.com/ddasturbek/LotinKrillYangiLotin/assets/76460501/a36715a4-2108-4179-b127-0409c5525708)

Harflarni almashtirishda foydalanilgan qoidalar manbalari:
1. [O‘zbek lotin alifbosi qoidalari](https://uz.wikipedia.org/wiki/Vikipediya:O%CA%BBzbek_lotin_alifbosi_qoidalari)
2. [Imlo va grammatika](https://uz.wikipedia.org/wiki/Vikipediya:Imlo_va_grammatika)

## Ee harfi

![Ee_Ye_Ээ_Ее](https://github.com/ddasturbek/LotinKrillYangiLotin/assets/76460501/1c251c4d-12dd-4b7a-80d8-a1ad463e79d5)

* Lotincha Ee harfi Krillchaga Ээ yoki Ее shaklida almashtiriladi.
* Lotincha Yeye harflar birikmasi esa Krillchaga faqat Ее shaklida almashtiriladi.
* Krillcha Ээ harfi Lotinchaga faqat Ee shaklida almashtiriladi.
* Krilcha Ее harfi Lotinchaga Ee yoki Yeye harf va harflar birikmasi shaklida almashtiriladi.

---

