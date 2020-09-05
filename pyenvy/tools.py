import subprocess
from typing import (
    Tuple,
    Optional,
)


def check_tool_paths() -> Tuple[Optional[str], Optional[str]]:
    """
    Attempts to locate `pyenv` and `poetry`.

    Utilizes `subprocess.run` in order to execute `which` on both
    `pyenv` and `poetry`.
    """
    pyenv = subprocess.run(["which", "pyenv"], capture_output=True)
    poetry = subprocess.run(["which", "poetry"], capture_output=True)

    if pyenv.returncode == 0:
        pyenv_path = pyenv.stdout.decode("UTF-8")
    else:
        pyenv_path = None

    if poetry.returncode == 0:
        poetry_path = poetry.stdout.decode("UTF-8")
    else:
        poetry_path = None

    return (pyenv_path, poetry_path)
