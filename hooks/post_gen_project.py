"""Yoinked from https://github.com/zillionare/python-project-wizard/blob/2d85c2c267f98e68288c3716d4e92c815e4cba33/hooks/post_gen_project.py.

Also see:
https://github.com/zillionare/python-project-wizard/blob/2d85c2c267f98e68288c3716d4e92c815e4cba33/hooks/aioproc.py.
"""

import asyncio
import contextlib
import functools
import os
import shlex
import sys
from asyncio.subprocess import Process
from collections.abc import Awaitable, Callable
from typing import ParamSpec, TypeVar

import colorama
from colorama import Fore, Style


async def _echo(stream: asyncio.StreamReader) -> None:
    while True:
        line_bytes = await stream.readline()
        line = line_bytes.decode("utf-8")
        if not line:
            break
        line = line.rstrip("\n")
        if line.upper().startswith("WARNING"):
            print(Fore.YELLOW + line + Style.RESET_ALL)
        elif line.upper().startswith("ERROR"):
            print(Fore.RED, line, Style.RESET_ALL)
            raise Exception(line)
        else:
            print(line)


P = ParamSpec("P")
R = TypeVar("R")


def async_run(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    """Handle async running of a function."""

    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Awaitable[R]:
        return asyncio.run(func(*args, **kwargs))  # type: ignore

    return wrapper


async def aioprocess(
    *cmds: str,
    stdout_handler: Callable = _echo,
    stderr_handler: Callable = _echo,
    inherit_env: bool = True,
    detached: bool = False,
    cwd: str | None = None,
) -> Process:
    """Execute cmds in asyncio process, and echo it's stdout/stderr.

    if detached is specified, the subprocess will be detached with parent after created.
    if inherit_env is specified, then subprocess with inherite envars from parent process.

    Args:
        *cmds: list of cmds to be executed
        stdout_handler: handler for stdout
        stderr_handler: handler for stderr
        inherit_env: inherit envars from parent process
        detached: detach subprocess with parent
        cwd: change working directory of subprocess
    Examples:
        >>> aioprocess("ls")
        >>> aioprocess("ping -c 10 www.baidu.com")
        >>> aioprocess("ping", "-c", "10", "www.baidu.com")
        >>> aioprocess("python -m http.server", detached=True)
    """
    cur_dir = os.getcwd()

    try:
        if cwd:
            os.chdir(cwd)

        if len(cmds) == 1 and isinstance(cmds[0], str):
            cmds = shlex.split(cmds[0])  # type: ignore[assignment]

        env = os.environ.copy() if inherit_env else None

        proc = await asyncio.create_subprocess_exec(
            *cmds,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            start_new_session=detached,
            env=env,
        )

        if stdout_handler:  # type: ignore[truthy-function]
            asyncio.ensure_future(stdout_handler(proc.stdout))
        if stderr_handler:  # type: ignore[truthy-function]
            asyncio.ensure_future(stderr_handler(proc.stderr))

        return proc
    finally:
        os.chdir(cur_dir)


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Delete a file if it exists."""
    with contextlib.suppress(FileNotFoundError):
        os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


@async_run
async def execute(*args: str, cwd: str | None = None) -> None:
    """Run a command in a directory."""
    os.getcwd()

    proc = await aioprocess(*args, cwd=cwd)
    await proc.wait()


def init_git() -> None:
    """Init the git repo."""
    if not os.path.exists(os.path.join(PROJECT_DIRECTORY, ".git")):
        execute("git", "init", cwd=PROJECT_DIRECTORY)
        execute(
            "git",
            "config",
            "user.name",
            "{{ cookiecutter.full_name }}",
            cwd=PROJECT_DIRECTORY,
        )
        execute(
            "git",
            "config",
            "user.email",
            "{{ cookiecutter.email }}",
            cwd=PROJECT_DIRECTORY,
        )


def init_dev() -> None:
    """Init all the dev stuff."""
    print(Style.NORMAL, Fore.BLUE, "creating virtualenv...")
    print(Style.RESET_ALL, Style.DIM)

    try:
        execute(sys.executable, "-m", "venv", ".venv")
    except Exception as e:
        print(e)
        print(
            Fore.YELLOW,
            f"failed to create virtual environment. You may need run `{sys.executable} -m venv .venv` "
            "later, if you want to use a venv",
            Style.RESET_ALL,
        )
    else:
        print(
            Style.NORMAL,
            Fore.GREEN,
            "virtual environment was successfully created",
            Style.RESET_ALL,
        )

    # print(Style.NORMAL, Fore.BLUE, "installing pre-commit hooks...")
    # print(Style.RESET_ALL, Style.DIM)
    # try:
    #     execute(EXECUTABLE, "-m", "pip", "install", "pre-commit")
    #     execute("pre-commit", "install", cwd=PROJECT_DIRECTORY)
    # except Exception as e:
    #     print(e)
    #     print(
    #         Fore.YELLOW,
    #         "failed to install pre-commit hooks. You may need run `pre-commit install` later",
    #         Style.RESET_ALL,
    #     )
    # else:
    #     print(Style.NORMAL, Fore.GREEN, "pre-commit hooks were successfully installed", Style.RESET_ALL)

    run_command = ["/usr/bin/env", "bash", "-c", ". .venv/bin/activate && poetry install"]

    try:
        print(Style.NORMAL, Fore.BLUE, "install all dev dependency packages...")
        print(Style.RESET_ALL, Style.DIM)
        execute(*run_command, cwd=PROJECT_DIRECTORY)
    except Exception as e:
        print(e)
        print(
            Style.NORMAL,
            Fore.YELLOW,
            "failed to install dev dependency packages, you may need re-run the task by yourself: " " ".join(
                run_command
            ),
            Style.RESET_ALL,
        )
    else:
        print(
            Style.NORMAL,
            Fore.GREEN,
            "all dev dependency packages installed successfully",
            Style.RESET_ALL,
        )

    run_command = ["/usr/bin/env", "bash", "scripts/export_requirements.sh"]

    try:
        print(Style.NORMAL, Fore.BLUE, "exporting requirements to files...")
        print(Style.RESET_ALL, Style.DIM)
        execute(*run_command, cwd=PROJECT_DIRECTORY)
    except Exception as e:
        print(e)
        print(
            Style.NORMAL,
            Fore.YELLOW,
            "failed to export requirements, you may need re-run the task by yourself: " " ".join(run_command),
            Style.RESET_ALL,
        )
    else:
        print(
            Style.NORMAL,
            Fore.GREEN,
            "all requirements exported successfully",
            Style.RESET_ALL,
        )

    run_command = ["/usr/bin/env", "bash", "scripts/lint-and-format.sh"]

    try:
        print(Style.NORMAL, Fore.BLUE, "running initial linting checks...")
        print(Style.RESET_ALL, Style.DIM)
        execute(*run_command, cwd=PROJECT_DIRECTORY)
    except Exception as e:
        print(e)
        print(
            Style.NORMAL,
            Fore.YELLOW,
            "initial linting checks failed, you may need re-run the task by yourself: " " ".join(run_command),
            Style.RESET_ALL,
        )
    else:
        print(
            Style.NORMAL,
            Fore.GREEN,
            "all linting checks passed successfully",
            Style.RESET_ALL,
        )

    if (
        "{{ cookiecutter.init_git_repo }}" == "y"  # type: ignore[comparison-overlap]
        and "{{ cookiecutter.init_dev_env_do_init_commit }}" == "y"  # type: ignore[comparison-overlap]
    ):
        try:
            print(Style.NORMAL, Fore.BLUE, "committing repo changes...")
            print(Style.RESET_ALL, Style.DIM)

            execute(
                "git",
                "add",
                ".",
                cwd=PROJECT_DIRECTORY,
            )
            execute(
                "git",
                "commit",
                "-m",
                "Initial commit",
                cwd=PROJECT_DIRECTORY,
            )
        except Exception as e:
            print(e)
            print(
                Style.NORMAL,
                Fore.YELLOW,
                "failed to commit changes, you may need commit the changes manually",
                Style.RESET_ALL,
            )
        else:
            print(
                Style.NORMAL,
                Fore.GREEN,
                "all changes committed successfully",
                Style.RESET_ALL,
            )


if __name__ == "__main__":
    colorama.init()

    if "{{ cookiecutter.open_source_license }}" == "Not open source":  # type: ignore[comparison-overlap]
        remove_file("LICENSE")

    if "{{ cookiecutter.init_git_repo }}" == "y":  # type: ignore[comparison-overlap]
        try:
            init_git()
        except Exception as e:
            print(e)

    if "{{ cookiecutter.init_dev_env }}" == "y":  # type: ignore[comparison-overlap]
        try:
            init_dev()
        except Exception as e:
            print(e)
