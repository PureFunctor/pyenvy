import unittest.mock as mock

from pyenvy.tools import check_tool_availability


def test_check_tool_availability(monkeypatch):
    pyenv_rc = mock.Mock(returncode=0)
    poetry_rc = mock.Mock(returncode=0)

    fake_run = mock.Mock(side_effect=[pyenv_rc, poetry_rc])

    monkeypatch.setattr("pyenvy.tools.subprocess.run", fake_run)

    assert check_tool_availability() == (True, True)


def test_check_tool_availability_no_pyenv(monkeypatch):
    pyenv_rc = mock.Mock(returncode=1)
    poetry_rc = mock.Mock(returncode=0)

    fake_run = mock.Mock(side_effect=[pyenv_rc, poetry_rc])

    monkeypatch.setattr("pyenvy.tools.subprocess.run", fake_run)

    assert check_tool_availability() == (False, True)


def test_check_tool_availability_no_poetry(monkeypatch):
    pyenv_rc = mock.Mock(returncode=0)
    poetry_rc = mock.Mock(returncode=1)

    fake_run = mock.Mock(side_effect=[pyenv_rc, poetry_rc])

    monkeypatch.setattr("pyenvy.tools.subprocess.run", fake_run)

    assert check_tool_availability() == (True, False)
