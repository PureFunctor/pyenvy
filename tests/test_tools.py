import unittest.mock as mock

from pyenvy.tools import check_tool_paths


def test_check_tool_paths(monkeypatch):
    pyenv = mock.Mock(returncode=0, stdout=b"/home/user/.pyenv/bin/pyenv")
    poetry = mock.Mock(returncode=0, stdout=b"/home/user/.poetry/bin/poetry")
    run = mock.Mock(side_effect=[pyenv, poetry])

    monkeypatch.setattr("pyenvy.tools.subprocess.run", run)

    assert check_tool_paths() == (pyenv.stdout.decode("UTF-8"), poetry.stdout.decode("UTF-8"))


def test_check_tool_paths_no_tools(monkeypatch):
    pyenv = mock.Mock(returncode=1, stdout=b"")
    poetry = mock.Mock(returncode=1, stdout=b"")
    run = mock.Mock(side_effect=[pyenv, poetry])

    monkeypatch.setattr("pyenvy.tools.subprocess.run", run)

    assert check_tool_paths() == (None, None)


def test_get_tool_paths_no_pyenv(monkeypatch):
    pyenv = mock.Mock(returncode=1, stdout=b"")
    poetry = mock.Mock(returncode=0, stdout=b"/home/user/.pyenv/bin/pyenv")
    run = mock.Mock(side_effect=[pyenv, poetry])

    monkeypatch.setattr("pyenvy.tools.subprocess.run", run)

    assert check_tool_paths() == (None, poetry.stdout.decode("UTF-8"))


def test_get_tool_paths_no_poetry(monkeypatch):
    pyenv = mock.Mock(returncode=0, stdout=b"/home/user/.pyenv/bin/pyenv")
    poetry = mock.Mock(returncode=1, stdout=b"")
    run = mock.Mock(side_effect=[pyenv, poetry])

    monkeypatch.setattr("pyenvy.tools.subprocess.run", run)

    assert check_tool_paths() == (pyenv.stdout.decode("UTF-8"), None)

