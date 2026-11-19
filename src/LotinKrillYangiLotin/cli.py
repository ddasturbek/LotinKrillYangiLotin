"""
Terminal buyrug‘i: ``lky`` (yoki ``python -m LotinKrillYangiLotin``).

Misollar::

    lky -t yangi kitob.txt -o kitob_yangi.txt
    lky -t krill -m "O‘zbekiston"
    echo "Шаҳар" | lky -t yangi
    lky --aniqlash kitob.txt
"""

from __future__ import annotations

import argparse
import sys

from . import __version__
from .core import detect_script, to_cyrillic, to_latin, to_new_latin

_MAQSADLAR = {
    "lotin": to_latin,
    "krill": to_cyrillic,
    "yangi": to_new_latin,
}
_MANBALAR = {"lotin": "latin", "yangi": "new_latin"}


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="lky",
        description="O‘zbek matnini Lotin, Krill va Yangi lotin (2027) yozuvlari o‘rtasida almashtirish.",
        epilog="Fayl ko‘rsatilmasa matn standart kirishdan (stdin) o‘qiladi.",
    )
    p.add_argument("fayllar", nargs="*", metavar="FAYL", help="kirish fayl(lar)i; '-' — stdin")
    p.add_argument(
        "-t", "--to", dest="maqsad", choices=sorted(_MAQSADLAR),
        help="maqsad yozuv: lotin, krill yoki yangi",
    )
    p.add_argument("-m", "--matn", help="faylsiz, to‘g‘ridan-to‘g‘ri matn")
    p.add_argument("-o", "--chiqish", metavar="FAYL", help="natijani faylga yozish (standart: stdout)")
    p.add_argument(
        "-s", "--manba", choices=sorted(_MANBALAR),
        help="lotin matn variantini majburan ko‘rsatish (Ö/Ğ/Ş/Ç bo‘lmagan yangi lotin matn uchun: yangi)",
    )
    p.add_argument("-a", "--aniqlash", action="store_true", help="faqat matn yozuvini aniqlash")
    p.add_argument("-V", "--version", action="version", version=f"%(prog)s {__version__}")
    return p


def _oqish(fayllar: list[str]) -> str:
    if not fayllar:
        fayllar = ["-"]
    qismlar = []
    for nom in fayllar:
        if nom == "-":
            qismlar.append(sys.stdin.read())
        else:
            with open(nom, encoding="utf-8-sig", newline="") as f:
                qismlar.append(f.read())
    return "".join(qismlar)


def main(argv: list[str] | None = None) -> int:
    for oqim in (sys.stdout, sys.stdin):
        if hasattr(oqim, "reconfigure"):
            oqim.reconfigure(encoding="utf-8")  # Windows konsoli uchun

    args = _parser().parse_args(argv)
    if not args.aniqlash and not args.maqsad:
        _parser().error("maqsad yozuvni ko‘rsating: -t lotin | krill | yangi (yoki --aniqlash)")
    if args.matn is not None and args.fayllar:
        _parser().error("-m/--matn va fayllarni birga ishlatib bo‘lmaydi")

    try:
        matn = args.matn if args.matn is not None else _oqish(args.fayllar)
    except OSError as e:
        print(f"lky: xato: {e}", file=sys.stderr)
        return 1

    if args.aniqlash:
        natija = detect_script(matn) + "\n"
    else:
        natija = _MAQSADLAR[args.maqsad](matn, source=_MANBALAR.get(args.manba))
        if args.matn is not None:
            natija += "\n"

    if args.chiqish:
        with open(args.chiqish, "w", encoding="utf-8", newline="") as f:
            f.write(natija)
    else:
        sys.stdout.write(natija)
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
