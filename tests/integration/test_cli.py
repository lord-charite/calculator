import builtins
from calculator.cli.main import main

def test_cli_divide_by_zero(monkeypatch, capsys):
    inputs = iter([
        "divide",
        "10",
        "0",
        "exit"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    code = main()
    out = capsys.readouterr().out

    assert "Cannot divide by zero" in out
    assert code == 0

def test_cli_add(monkeypatch, capsys):
    inputs = iter([
        "add",
        "2",
        "3",
        "exit"
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    code = main()
    out = capsys.readouterr().out

    assert "Result: 5.0" in out  # because you cast to float
    assert code == 0