import subprocess
from typing import Tuple


def check_tool_availability() -> Tuple[bool, bool]:
    """
    Checks the availability of `pyenv` and `poetry`.

    Utilizes `subprocess.run` in order to execute `which` on both
    `pyenv` and `poetry`.
    """
    pyenv_rc = subprocess.run(["which", "pyenv"], capture_output=True).returncode
    poetry_rc = subprocess.run(["which", "poetry"], capture_output=True).returncode

    return (not pyenv_rc, not poetry_rc)
