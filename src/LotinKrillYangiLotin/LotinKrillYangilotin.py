"""
v1 bilan moslik qatlami.

``Almashtirish`` klassi 2.x versiyalarida eskirgan (deprecated) hisoblanadi va
3.0.0 da olib tashlanadi. Uning o‘rniga funksiyalardan foydalaning::

    from LotinKrillYangiLotin import to_latin, to_cyrillic, to_new_latin

Eslatma: 2.0.0 dan boshlab ``YangiLotinga`` O‘RQ-1184 qonunidagi harflarni
qaytaradi (Ö ö, Ğ ğ), v1 dagi Ō ō, Ḡ ḡ emas.
"""

import warnings

from .core import to_cyrillic, to_latin, to_new_latin

__all__ = ["Almashtirish"]


def _ogohlantir(eski: str, yangi: str) -> None:
    warnings.warn(
        f"Almashtirish.{eski}() eskirgan, uning o‘rniga {yangi}() dan foydalaning. "
        "Almashtirish klassi 3.0.0 versiyada olib tashlanadi.",
        DeprecationWarning,
        stacklevel=3,
    )


class Almashtirish:
    """Eskirgan: o‘rniga ``to_latin``, ``to_cyrillic``, ``to_new_latin`` funksiyalari."""

    def Lotinga(self, text):  # noqa: N802
        _ogohlantir("Lotinga", "to_latin")
        return to_latin(text)

    def Krillga(self, text):  # noqa: N802
        _ogohlantir("Krillga", "to_cyrillic")
        return to_cyrillic(text)

    def YangiLotinga(self, text):  # noqa: N802
        _ogohlantir("YangiLotinga", "to_new_latin")
        return to_new_latin(text)
