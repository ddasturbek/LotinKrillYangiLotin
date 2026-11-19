"""
Istisnolar lug‘ati — qoidalar bilan aniqlab bo‘lmaydigan so‘zlar.

Kalitlar yangi lotin "fonema" shaklida, kichik harflarda yoziladi
(ş, ç, ö, ğ, tutuq ’). Har bir yozuv **o‘zak** hisoblanadi: unga o‘zbekcha
qo‘shimchalar (-lar, -ni, -da, -dagi, -i, -imiz ...) qo‘shilgan shakllar ham taniladi.

Yangi so‘z qo‘shish uchun shu fayldagi lug‘atlarga qator qo‘shing va
``tests/test_lugat.py`` ga misol yozing.
"""

#: Lotin → Krill: ь, ц va boshqa qoidaga sig‘maydigan o‘zlashma so‘zlar.
#: Krill qiymatidagi oxirgi ``ь`` so‘zga qo‘shimcha qo‘shilganda tushiriladi
#: (sentabr → сентябрь, sentabrda → сентябрда).
LOTIN_KRILL = {
    # Oylar
    "yanvar": "январь",
    "fevral": "февраль",
    "aprel": "апрель",
    "iyun": "июнь",
    "iyul": "июль",
    "sentabr": "сентябрь",
    "oktabr": "октябрь",
    "noyabr": "ноябрь",
    "dekabr": "декабрь",
    # ь belgili o‘zlashmalar
    "albom": "альбом",
    "avtomobil": "автомобиль",
    "film": "фильм",
    "kalendar": "календарь",
    "kalsiy": "кальций",
    "kompyuter": "компьютер",
    "intervyu": "интервью",
    "medal": "медаль",
    "mebel": "мебель",
    "model": "модель",
    "poçtalyon": "почтальон",
    "portfel": "портфель",
    "rol": "роль",
    "tonnel": "тоннель",
    "şampun": "шампунь",
    "pyesa": "пьеса",
    "sekretar": "секретарь",
    "spektakl": "спектакль",
    # ц bilan yoziladigan o‘zlashmalar
    "sirk": "цирк",
    "sement": "цемент",
    "sex": "цех",
    "sentner": "центнер",
    "sink": "цинк",
    "silindr": "цилиндр",
    "sikl": "цикл",
    "sitata": "цитата",
    "sitrus": "цитрус",
    "konsert": "концерт",
    "konsern": "концерн",
    "prinsip": "принцип",
    "stansiya": "станция",
    "instansiya": "инстанция",
    "distansiya": "дистанция",
    "kvitansiya": "квитанция",
    "provinsiya": "провинция",
    "konferensiya": "конференция",
    "tendensiya": "тенденция",
    "kompetensiya": "компетенция",
    # э bilan yoziladigan so‘zlar (undoshdan keyin)
    "mer": "мэр",
    # Qoidaga qarshi: p+siya odatda пция, lekin bular с bilan
    "epilepsiya": "эпилепсия",
}

#: Krill → Lotin: qoidalar natijasini to‘g‘rilash (kalit — qoidadan chiqqan shakl).
#: Bu yerda o‘zak prefiks sifatida mos keladi (qo‘shimcha ro‘yxati tekshirilmaydi).
KRILL_LOTIN = {
    "sentyabr": "sentabr",   # сентябрь
    "oktyabr": "oktabr",     # октябрь
    "obekt": "obyekt",       # обект (keng tarqalgan xato yozuv) → obyekt
    "lvov": "livov",         # Львов
}
