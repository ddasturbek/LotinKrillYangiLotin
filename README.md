## Dastur haqida
**Muallif: [Dasturbek](https://github.com/ddasturbek)**

**Versiya: 1.0.0**

Dasturdan o‘zbek tilidagi matnlarni yozuv shaklini almashtirishda va yangi lotin alifbosini joriy qilishda foydalanish mumkin!

## Dasturni o‘rnatish

Siz dasturni Python loyihangizga [pip](https://pypi.org/project/LotinKrillYangiLotin) orqali o‘rnatib foydalanishingiz mumkin.

```bash
pip install LotinKrillYangiLotin
```

Yoki [githubdan](https://github.com/ddasturbek/LotinKrillYangiLotin) klonlab foydalanishingiz mumkin.

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

**Krillcha Eе harfini lotinchaga o‘zgartirish qoidalari.**

1) So‘zning boshida yoki unlidan keyin kelsa ye shaklida: егулик - yegulik, поезд - poyezd; ъ tutuq belgisidan keyin kelsa ъ olib tashlanadi va ye shaklida: подъезд - podyezd

2) Qolgan barcha holatlarda lotincha Ee shaklida o‘zgartiriladi.


**Lotinchada Ee harfini krillchaga o‘zgartirish qoidalari.**
1) So‘zning boshida va unlidan keyin kelsa Ээ shaklida: elak-элак, aeraport-аэропорт

2) Undosh harfidan keyin kelsa Ее shaklida: temir-темир, kel-кел, geometriya-геометрия; Yy undoshidan keyin kelsa Yy tushirib qoldirilib Ее shaklida yoziladi: yengil-енгил
---

## Dasturni testlash natijalari

Dasturni testlab ko‘rish uchun wikipediadan quyidagi [matn](https://uz.wikipedia.org/w/index.php?title=Til) olindi (lotin va krillcha holatlarda).

| Yozuv shakli | 	Belgilar soni |	Matndagi birinchi gap.                                                                           |
|--------------|----------------|--------------------------------------------------------------------------------------------------|
| [Lotin](https://github.com/ddasturbek/LotinKrillYangiLotin/blob/main/data/Til_Lotin.txt)        |	8623          |	Til deb murakkab muloqot tizimiga yoki shu tizimni oʻrganish va ishlatish qobiliyatiga aytiladi. |
| [Krill](https://github.com/ddasturbek/LotinKrillYangiLotin/blob/main/data/Til_Krill.txt)	       |  8217          |	Тил деб мураккаб мулоқот тизимига ёки шу тизимни ўрганиш ва ишлатиш қобилиятига айтилади.        |
| [Yangi lotin](https://github.com/ddasturbek/LotinKrillYangiLotin/blob/main/data/Til_YangiLotin.txt)	 |  8319        	| Til deb murakkab muloqot tizimiga yoki şu tizimni ōrganiş va işlatiş qobiliyatiga aytiladi.      |

Bu manbadagi matn Yangi lotin yozuvida mavjud emas, shuning uchun uni Notepad dasturi orqali quyidagi harflari **O‘o‘G‘g‘ShshChch -> ŌōḠḡŞşÇç** ga almashtirildi va ushbu matn ham boshqa shakllar kabi fayl qilib testlash uchun saqlab olindi.

![Test natijalari](https://github.com/ddasturbek/LotinKrillYangiLotin/assets/76460501/0c3568b9-c3d7-4c91-a2ac-68bbe72d1b42)

[1] **обектив=obyektiv** Turli manbalarda turlicha yozilgan: ob’ekt [dastur bu holatda to‘g‘ri ishlaydi].

Krillcha **обектив** so‘zi Lotin va Yangi Lotinga almashtirilganda **obektiv** shaklida alamshib qoldi, bunga sabab qoidalar, aslida Lotin va Yangi lotinda **obyektiv** bo‘lishi kerak.

Boshqa almashtirishlarda bunday holat kuzatilmadi, chunki boshqa Krillcha harflarda Ee harfi qoidalarga mos ravishda almashadi, ya’ni uning oldida keladigan so‘zga bog‘liq. 

## Patent

![Guvohnoma](https://github.com/user-attachments/assets/503150f3-43b1-4693-986b-6333446b9299)
