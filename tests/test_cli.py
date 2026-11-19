"""lky terminal buyrug‘i testlari."""

import io
import subprocess
import sys

import pytest

from LotinKrillYangiLotin.cli import main


def _ishlat(argv, stdin="", monkeypatch=None):
    out = io.StringIO()
    monkeypatch.setattr(sys, "stdin", io.StringIO(stdin))
    monkeypatch.setattr(sys, "stdout", out)
    kod = main(argv)
    return kod, out.getvalue()


def test_matn(monkeypatch):
    assert _ishlat(["-t", "krill", "-m", "O‘zbekiston"], monkeypatch=monkeypatch) == (0, "Ўзбекистон\n")


def test_stdin(monkeypatch):
    assert _ishlat(["-t", "yangi"], stdin="Шаҳар\n", monkeypatch=monkeypatch) == (0, "Şahar\n")


def test_manba(monkeypatch):
    assert _ishlat(["-t", "krill", "-s", "yangi", "-m", "Ishoq"], monkeypatch=monkeypatch)[1] == "Исҳоқ\n"


def test_aniqlash(monkeypatch):
    assert _ishlat(["--aniqlash", "-m", "şahar"], monkeypatch=monkeypatch)[1] == "new_latin\n"


def test_fayldan_faylga(tmp_path, monkeypatch):
    kirish = tmp_path / "k.txt"
    chiqish = tmp_path / "ch.txt"
    kirish.write_bytes("Чой\r\nўғил\r\n".encode("utf-8-sig"))  # BOM va CRLF
    kod, out = _ishlat(["-t", "yangi", str(kirish), "-o", str(chiqish)], monkeypatch=monkeypatch)
    assert kod == 0 and out == ""
    assert chiqish.read_bytes().decode("utf-8") == "Çoy\r\nöğil\r\n"


def test_fayl_topilmadi(tmp_path, monkeypatch, capsys):
    kod, _ = _ishlat(["-t", "lotin", str(tmp_path / "yoq.txt")], monkeypatch=monkeypatch)
    assert kod == 1


@pytest.mark.parametrize("argv", [[], ["-m", "x"], ["-t", "arab", "-m", "x"]])
def test_notogri_parametrlar(argv, monkeypatch):
    with pytest.raises(SystemExit) as e:
        _ishlat(argv, monkeypatch=monkeypatch)
    assert e.value.code == 2


def test_python_m():
    natija = subprocess.run(
        [sys.executable, "-m", "LotinKrillYangiLotin", "-t", "yangi", "-m", "чой"],
        capture_output=True, encoding="utf-8", check=True,
    )
    assert natija.stdout == "çoy\n"
