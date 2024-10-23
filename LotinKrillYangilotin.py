"""
    Muallif: Dasturbek (github.com/ddasturbek)
    Versiya: 1.0.0

    Dasturdan o‘zbek tilidagi matnlarni yozuv shaklini almashtirishda
    va yangi lotin alifbosini joriy qilishda foydalanish mumkin!

    O‘zbek Lotin alifbosida 29 harf va bitta tutuq belgi (’) bor.
    O‘zbek Krill alifbosida shunga mos, ya’ni 30 ta harf va belgi bor.
    O‘zbek Yangi lotin alifbosida ham jami 30 ta harf va belgi bor.

    Alifbo bilan to‘liq holda quyida tanishishingiz mumkin:
    https://github.com/ddasturbek/LotinKrillYangiLotin/assets/76460501/a36715a4-2108-4179-b127-0409c5525708

    Yangi lotin yozuvi haqida O‘zbekiston Respublikasi Fanlar akademiyasi tomonidan 'NORMATIV-HUQUQIY HUJJATLAR LOYIHALARI MUHOKAMASI PORTALI'ga muhokamaga qo‘yilgan:
    https://regulation.gov.uz/oz/d/31596

    Harflarni almashtirishda foydalanilgan qoidalar manbalari:
    1. https://uz.wikipedia.org/wiki/Vikipediya:O%CA%BBzbek_lotin_alifbosi_qoidalari
    2. https://uz.wikipedia.org/wiki/Vikipediya:Imlo_va_grammatika

"""


class Almashtirish:

    def __init__(self):
        self.__LotinAlifbo = "AaBbDdFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYyZz’’"  # EeO‘o‘G‘g‘ShshChchNgng
        self.__KrillAlifbo = "АаБбДдФфГгҲҳИиЖжКкЛлМмНнОоПпҚқРрСсТтУуВвХхЙйЗзЪъ"  # ЕеЎўҒғШшЧчНгнг + ЭэЁёЦцЮюЯя
        self.__YangiLotinAlifbo = "AaBbDdFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvXxYyZz’’"  # EeŌōḠḡŞşÇçng

    @staticmethod
    def __change_apostrophe(text):
        # Function to change the character of the letters O‘o‘ and G‘g‘

        text = text.replace(f"O{chr(39)}", f"O{chr(8216)}")  # ord("'") -> ord("‘")
        text = text.replace(f"o{chr(39)}", f"o{chr(8216)}")
        text = text.replace(f"G{chr(39)}", f"G{chr(8216)}")
        text = text.replace(f"g{chr(39)}", f"g{chr(8216)}")

        text = text.replace(f"O{chr(96)}", f"O{chr(8216)}")  # ord("`") -> ord("‘")
        text = text.replace(f"o{chr(96)}", f"o{chr(8216)}")
        text = text.replace(f"G{chr(96)}", f"G{chr(8216)}")
        text = text.replace(f"g{chr(96)}", f"g{chr(8216)}")

        text = text.replace(f"O{chr(699)}", f"O{chr(8216)}")  # ord("ʻ") -> ord("‘")
        text = text.replace(f"o{chr(699)}", f"o{chr(8216)}")
        text = text.replace(f"G{chr(699)}", f"G{chr(8216)}")
        text = text.replace(f"g{chr(699)}", f"g{chr(8216)}")

        text = text.replace(f"O{chr(700)}", f"O{chr(8216)}")  # ord("ʼ") -> ord("‘")
        text = text.replace(f"o{chr(700)}", f"o{chr(8216)}")
        text = text.replace(f"G{chr(700)}", f"G{chr(8216)}")
        text = text.replace(f"g{chr(700)}", f"g{chr(8216)}")

        text = text.replace(f"O{chr(8217)}", f"O{chr(8216)}")  # ord("’") -> ord("‘")
        text = text.replace(f"o{chr(8217)}", f"o{chr(8216)}")
        text = text.replace(f"G{chr(8217)}", f"G{chr(8216)}")
        text = text.replace(f"g{chr(8217)}", f"g{chr(8216)}")

        return text

    def Lotinga(self, text):  # noqa
        result = ""
        text = self.__change_apostrophe(text)
        for i in range(len(text)):
            if i == 0 and ord(text[i]) == ord('Е'):
                if text.isupper():
                    result += "YE"
                else:
                    result += "Ye"
            elif i == 0 and ord(text[i]) == ord('е'):
                result += "ye"
            elif i > 0 and text[i - 1] in [' ', 'А', 'E', 'И', 'О', 'У', 'Ў', 'Ъ', '-'] and ord(text[i]) == ord('Е'):
                if text[i - 1] == 'Ъ':
                    result = result[:-1]
                if text.isupper():
                    result += "YE"
                else:
                    result += "Ye"
            elif i > 0 and text[i - 1] in [' ', 'а', 'е', 'и', 'о', 'у', 'ў', 'ъ', '-'] and ord(text[i]) == ord('е'):
                if text[i - 1] == 'ъ':
                    result = result[:-1]
                result += "ye"
            elif ord(text[i]) == ord('Е'):
                result += "E"
            elif ord(text[i]) == ord('е'):
                result += "e"
            elif ord(text[i]) == ord('Э'):
                result += "E"
            elif ord(text[i]) == ord('э'):
                result += "e"
            elif ord(text[i]) == ord('С'):
                result += "S"
            elif ord(text[i]) == ord('с'):
                result += "s"
            elif ord(text[i]) == ord('Ў'):
                result += "O‘"
            elif ord(text[i]) == ord('ў'):
                result += "o‘"
            elif ord(text[i]) == ord('Ғ'):
                result += "G‘"
            elif ord(text[i]) == ord('ғ'):
                result += "g‘"
            elif ord(text[i]) == ord('Ш'):
                if text.isupper():
                    result += "SH"
                else:
                    result += "Sh"
            elif ord(text[i]) == ord('ш'):
                result += "sh"
            elif ord(text[i]) == ord('Ч'):
                if text.isupper():
                    result += "CH"
                else:
                    result += "Ch"
            elif ord(text[i]) == ord('ч'):
                result += "ch"
            elif ord(text[i]) == ord('Ō'):
                result += "O‘"
            elif ord(text[i]) == ord('ō'):
                result += "o‘"
            elif ord(text[i]) == ord('Ḡ'):
                result += "G‘"
            elif ord(text[i]) == ord('ḡ'):
                result += "g‘"
            elif ord(text[i]) == ord('Ş'):
                if text.isupper():
                    result += "SH"
                else:
                    result += "Sh"
            elif ord(text[i]) == ord('ş'):
                result += "sh"
            elif ord(text[i]) == ord('Ç'):
                if text.isupper():
                    result += "CH"
                else:
                    result += "Ch"
            elif ord(text[i]) == ord('ç'):
                result += "ch"
            elif ord(text[i]) == ord('Ё'):
                if text.isupper():
                    result += "YO"
                else:
                    result += "Yo"
            elif ord(text[i]) == ord('ё'):
                result += "yo"
            elif i > 0 and text[i - 1] in ['А', 'E', 'И', 'О', 'У', 'Ў'] and ord(text[i]) == ord('Ц'):
                if text.isupper():
                    result += "TS"
                else:
                    result += "Ts"
            elif i > 0 and text[i - 1] in ['а', 'е', 'и', 'о', 'у', 'ў'] and ord(text[i]) == ord('ц'):
                result += "ts"
            elif ord(text[i]) == ord('Ц'):
                result += "S"
            elif ord(text[i]) == ord('ц'):
                result += "s"
            elif ord(text[i]) == ord('Ю'):
                if text.isupper():
                    result += "YU"
                else:
                    result += "Yu"
            elif ord(text[i]) == ord('ю'):
                result += "yu"
            elif ord(text[i]) == ord('Я'):
                if text.isupper():
                    result += "YA"
                else:
                    result += "Ya"
            elif ord(text[i]) == ord('я'):
                result += "ya"
            elif self.__KrillAlifbo.find(text[i]) + 1:
                result += self.__LotinAlifbo[self.__KrillAlifbo.find(text[i])]
            else:
                result += text[i]

        return result

    def Krillga(self, text):  # noqa
        result = ""
        text = self.__change_apostrophe(text)
        for i in range(len(text)):
            if i == 0 and ord(text[i]) == ord('E'):
                result += "Э"
            elif i == 0 and ord(text[i]) == ord('e'):
                result += "э"
            elif i > 0 and text[i - 1] == ' ' and ord(text[i]) == ord('E'):
                result += "Э"
            elif i > 0 and text[i - 1] == ' ' and ord(text[i]) == ord('e'):
                result += "э"
            elif i > 0 and text[i - 1] in ['A', 'E', 'I', 'O', 'U'] and ord(text[i]) == ord('E'):
                result += "Э"
            elif i > 0 and text[i - 1] in ['a', 'e', 'i', 'o', 'u'] and ord(text[i]) == ord('e'):
                result += "э"
            elif i > 1 and text[i - 2] == 'O' and text[i - 1] == '‘' and ord(text[i]) == ord('E'):
                result += "Э"
            elif i > 1 and text[i - 2] == 'o' and text[i - 1] == '‘' and ord(text[i]) == ord('e'):
                result += "э"
            elif i > 0 and ord(text[i - 1]) == ord('Y') and ord(text[i]) == ord('E'):
                result = result[:-1]
                result += "Е"
            elif i > 0 and ord(text[i - 1]) == ord('y') and ord(text[i]) == ord('e'):
                result = result[:-1]
                result += "е"
            elif ord(text[i]) == ord('E'):
                result += "Е"
            elif ord(text[i]) == ord('e'):
                result += "е"
            elif i > 0 and text[i - 1] == 'O' and text[i] == '‘':
                if result[len(result)-1] == 'Ё':
                    result = result[:-1]
                    result += "ЙЎ"
                else:
                    result = result[:-1]
                    result += "Ў"
            elif i > 0 and text[i - 1] == 'o' and text[i] == '‘':
                if result[len(result)-1] == 'ё':
                    result = result[:-1]
                    result += "йў"
                else:
                    result = result[:-1]
                    result += "ў"
            elif i > 0 and text[i - 1] == 'G' and text[i] == '‘':
                result = result[:-1]
                result += "Ғ"
            elif i > 0 and text[i - 1] == 'g' and text[i] == '‘':
                result = result[:-1]
                result += "ғ"
            elif i > 0 and text[i - 1] == "S" and (ord(text[i]) == ord('H') or ord(text[i]) == ord('h')):
                result = result[:-1]
                result += "Ш"
            elif i > 0 and text[i - 1] == "s" and ord(text[i]) == ord('h'):
                result = result[:-1]
                result += "ш"
            elif i > 0 and text[i - 1] == "C" and (ord(text[i]) == ord('H') or ord(text[i]) == ord('h')):
                result = result[:-1]
                result += "Ч"
            elif i > 0 and text[i - 1] == "c" and ord(text[i]) == ord('h'):
                result = result[:-1]
                result += "ч"
            elif ord(text[i]) == ord('Ō'):
                result += "Ў"
            elif ord(text[i]) == ord('ō'):
                result += "ў"
            elif ord(text[i]) == ord('Ḡ'):
                result += "Ғ"
            elif ord(text[i]) == ord('ḡ'):
                result += "ғ"
            elif ord(text[i]) == ord('Ş'):
                result += "Ш"
            elif ord(text[i]) == ord('ş'):
                result += "ш"
            elif ord(text[i]) == ord('Ç'):
                result += "Ч"
            elif ord(text[i]) == ord('ç'):
                result += "ч"
            elif i > 0 and text[i - 1] == 'Y' and (ord(text[i]) == ord('O') or ord(text[i]) == ord('o')):
                result = result[:-1]
                result += "Ё"
            elif i > 0 and text[i - 1] == 'y' and ord(text[i]) == ord('o'):
                result = result[:-1]
                result += "ё"
            elif i > 0 and text[i-1] == 'T' and (text[i] == 'S' or text[i] == 's'):
                result = result[:-1]
                result += "Ц"
            elif i > 0 and text[i - 1] == 't' and ord(text[i]) == ord('s'):
                result = result[:-1]
                result += "ц"
            elif i > 0 and text[i - 1] == 'Y' and (ord(text[i]) == ord('U') or ord(text[i]) == ord('u')):
                result = result[:-1]
                result += "Ю"
            elif i > 0 and text[i - 1] == 'y' and ord(text[i]) == ord('u'):
                result = result[:-1]
                result += "ю"
            elif i > 0 and text[i - 1] == 'Y' and (ord(text[i]) == ord('A') or ord(text[i]) == ord('a')):
                result = result[:-1]
                result += "Я"
            elif i > 0 and text[i - 1] == 'y' and ord(text[i]) == ord('a'):
                result = result[:-1]
                result += "я"
            elif ord(text[i]) == ord("'") or ord(text[i]) == ord("`") or ord(text[i]) == ord("ʻ") or ord(text[i]) == ord("ʼ") or ord(text[i]) == ord("‘") or ord(text[i]) == ord("’"):
                if text.isupper():
                    result += "Ъ"
                else:
                    result += "ъ"
            elif self.__LotinAlifbo.find(text[i]) + 1:
                result += self.__KrillAlifbo[self.__LotinAlifbo.find(text[i])]
            else:
                result += text[i]

        return result

    def YangiLotinga(self, text):  # noqa
        result = ""
        text = self.__change_apostrophe(text)
        for i in range(len(text)):
            if i == 0 and ord(text[i]) == ord('Е'):
                if text.isupper():
                    result += "YE"
                else:
                    result += "Ye"
            elif i == 0 and ord(text[i]) == ord('е'):
                result += "ye"
            elif i > 0 and text[i - 1] in [' ', 'А', 'E', 'И', 'О', 'У', 'Ў', 'Ъ'] and ord(text[i]) == ord('Е'):
                if text[i - 1] == 'Ъ':
                    result = result[:-1]
                if text.isupper():
                    result += "YE"
                else:
                    result += "Ye"
            elif i > 0 and text[i - 1] in [' ', 'а', 'е', 'и', 'о', 'у', 'ў', 'ъ'] and ord(text[i]) == ord('е'):
                if text[i - 1] == 'ъ':
                    result = result[:-1]
                result += "ye"
            elif ord(text[i]) == ord('Е'):
                result += "E"
            elif ord(text[i]) == ord('е'):
                result += "e"
            elif ord(text[i]) == ord('Э'):
                result += "E"
            elif ord(text[i]) == ord('э'):
                result += "e"
            elif ord(text[i]) == ord('С'):
                result += "S"
            elif ord(text[i]) == ord('с'):
                result += "s"
            elif ord(text[i]) == ord('Ў'):
                result += "Ō"
            elif ord(text[i]) == ord('ў'):
                result += "ō"
            elif ord(text[i]) == ord('Ғ'):
                result += "Ḡ"
            elif ord(text[i]) == ord('ғ'):
                result += "ḡ"
            elif i > 0 and text[i - 1] == 'O' and text[i] == '‘':
                result = result[:-1]
                result += "Ō"
            elif i > 0 and text[i - 1] == 'o' and text[i] == '‘':
                result = result[:-1]
                result += "ō"
            elif i > 0 and text[i - 1] == 'G' and text[i] == '‘':
                result = result[:-1]
                result += "Ḡ"
            elif i > 0 and text[i - 1] == 'g' and text[i] == '‘':
                result = result[:-1]
                result += "ḡ"
            elif ord(text[i]) == ord('Ш'):
                result += "Ş"
            elif ord(text[i]) == ord('ш'):
                result += "ş"
            elif ord(text[i]) == ord('Ч'):
                result += "Ç"
            elif ord(text[i]) == ord('ч'):
                result += "ç"
            elif i > 0 and text[i - 1] == "S" and (ord(text[i]) == ord('H') or ord(text[i]) == ord('h')):
                result = result[:-1]
                result += "Ş"
            elif i > 0 and text[i - 1] == "s" and ord(text[i]) == ord('h'):
                result = result[:-1]
                result += "ş"
            elif i > 0 and text[i - 1] == "C" and (ord(text[i]) == ord('H') or ord(text[i]) == ord('h')):
                result = result[:-1]
                result += "Ç"
            elif i > 0 and text[i - 1] == "c" and ord(text[i]) == ord('h'):
                result = result[:-1]
                result += "ç"
            elif ord(text[i]) == ord('Ё'):
                if text.isupper():
                    result += "YO"
                else:
                    result += "Yo"
            elif ord(text[i]) == ord('ё'):
                result += "yo"
            elif i > 0 and text[i - 1] in ['А', 'E', 'И', 'О', 'У', 'Ў'] and ord(text[i]) == ord('Ц'):
                if text.isupper():
                    result += "TS"
                else:
                    result += "Ts"
            elif i > 0 and text[i - 1] in ['а', 'е', 'и', 'о', 'у', 'ў'] and ord(text[i]) == ord('ц'):
                result += "ts"
            elif ord(text[i]) == ord('Ц'):
                result += "S"
            elif ord(text[i]) == ord('ц'):
                result += "s"
            elif ord(text[i]) == ord('Ю'):
                if text.isupper():
                    result += "YU"
                else:
                    result += "Yu"
            elif ord(text[i]) == ord('ю'):
                result += "yu"
            elif ord(text[i]) == ord('Я'):
                if text.isupper():
                    result += "YA"
                else:
                    result += "Ya"
            elif ord(text[i]) == ord('я'):
                result += "ya"
            elif self.__KrillAlifbo.find(text[i]) + 1:
                result += self.__YangiLotinAlifbo[self.__KrillAlifbo.find(text[i])]
            else:
                result += text[i]

        return result
