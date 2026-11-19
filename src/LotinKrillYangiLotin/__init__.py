"""
    LotinKrillYangiLotin — o‘zbek tili uchun Lotin, Krill va Yangi lotin
    (O‘RQ-1184, 2027-yil 22-apreldan) yozuvlari o‘rtasida transliteratsiya.

    Muallif: Dasturbek (github.com/ddasturbek)

    >>> from LotinKrillYangiLotin import to_new_latin
    >>> to_new_latin("Шоир ўғил")
    'Şoir öğil'
"""

from .core import OKINA, TUTUQ, detect_script, to_cyrillic, to_latin, to_new_latin
from .LotinKrillYangilotin import Almashtirish

__version__ = "2.0.0"

__all__ = [
    "to_latin",
    "to_cyrillic",
    "to_new_latin",
    "detect_script",
    "TUTUQ",
    "OKINA",
    "Almashtirish",
    "__version__",
]
