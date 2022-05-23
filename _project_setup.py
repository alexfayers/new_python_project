import pathlib
import sys
import argparse


# OLD VALUES
REPLACEMENT_BASE = "NEW_PROJECT"
REPLACE_KEYS = ["NAME", "AUTHOR", "DESCRIPTION"]

LIVE_MODE = False


def load_replacement_values() -> dict[str, str]:
    """Load new project information from the cli.

    Returns:
        dict[str, str]: The replacement map to be used in `replace_placeholders`
    """
    parser = argparse.ArgumentParser()
    for value in REPLACE_KEYS:
        parser.add_argument(
            f"{value.lower()}", type=str, help=f"New {value} for project"
        )
    parser.add_argument(
        "-l", "--live", action="store_true", help="Perform live replacements"
    )

    args = parser.parse_args()

    REPLACE_MAP = {}

    for key in reversed(REPLACE_KEYS):
        new_key = f"{REPLACEMENT_BASE}_{key}".lower()
        REPLACE_MAP[new_key] = getattr(args, key.lower(), None)
        if REPLACE_MAP[new_key] is None:
            print(f"ERROR: {key.lower()} argument is not set")
            sys.exit(1)

    return REPLACE_MAP  # type: ignore


def path_recurse_directories(path: pathlib.Path) -> list[pathlib.Path]:
    """Recursively list all directories in a given path.

    Args:
        path (pathlib.Path): The path to recurse

    Returns:
        list[pathlib.Path]: A list of all directories in the given path
    """
    directories = [
        current_path
        for current_path in path.glob("*")
        if current_path.is_dir()
        and not current_path.name.startswith(".")
        and not current_path.name.startswith("__")
        and not current_path.name.endswith("egg-info")
    ]

    for directory in directories:
        directories.extend(path_recurse_directories(directory))

    return directories


def replace_placeholders(REPLACE_MAP: dict[str, str]) -> None:
    """Initialise the project by replacing the template placeholders with the new values.

    Args:
        REPLACE_MAP (dict[str, str]): The replacement map generated within `load_replacement_values`
    """
    PROJECT_PATH = pathlib.Path(__file__).parent
    NEW_PROJECT_NAME = REPLACE_MAP[f"{REPLACEMENT_BASE}_NAME".lower()]

    search_directories: list[pathlib.Path] = path_recurse_directories(PROJECT_PATH)
    search_directories.append(PROJECT_PATH)

    replace_files = []
    DO_NOT_REPLACE = [
        PROJECT_PATH / pathlib.Path("setup.py"),
        PROJECT_PATH / pathlib.Path("LICENSE"),
        PROJECT_PATH / pathlib.Path(".gitignore"),
    ]

    for directory in search_directories:
        for current_path in directory.glob("*"):
            if (
                current_path.is_file()
                and not current_path.samefile(pathlib.Path(__file__))
                and current_path not in DO_NOT_REPLACE
            ):
                replace_files.append(current_path)

    # replace placeholders in files
    success_count = 0
    print("[File content replace]\t@@ Replacing placeholders in files...")
    for target_file in replace_files:
        replacements = 0
        try:
            file_text = target_file.read_text()
        except UnicodeDecodeError:
            continue

        for key, value in REPLACE_MAP.items():
            key_replacements = 0
            while key in file_text:
                file_text = file_text.replace(key, value, 1)
                key_replacements += 1
            if key_replacements > 0:
                print(
                    "[File content replace]\t\t"
                    f"Replacing {key_replacements} instance{'s' if key_replacements > 1 else ''}"
                    f"of '{key}' with '{value}' in '{target_file}'"
                )
                replacements += key_replacements

        if replacements > 0:
            if LIVE_MODE:
                target_file.write_text(file_text)
            success_count += 1

    if success_count <= 0:
        print("[File content replace]\t@@ No placeholders replaced.")
    else:
        print(
            f"[File content replace]\t@@ {success_count} placeholder{'s' if success_count > 1 else ''} replaced."
        )

    # rename files
    success_count = 0
    print("[File rename]\t\t@@ Looking for files to rename...")
    for target_file in replace_files:
        if target_file.stem.lower() == f"{REPLACEMENT_BASE}_NAME".lower():
            print(
                "[File rename]\t\t\t"
                f"Renaming '{target_file}' to '{target_file.parent / f'{NEW_PROJECT_NAME}{target_file.suffix}'}'"
            )
            if LIVE_MODE:
                target_file.rename(
                    target_file.parent / f"{NEW_PROJECT_NAME}{target_file.suffix}"
                )
            success_count += 1

    if success_count <= 0:
        print("[File rename]\t\t@@ No files renamed.")
    else:
        print(
            f"[File rename]\t\t@@ {success_count} file{'s' if success_count > 1 else ''} renamed."
        )

    # rename directories
    success_count = 0
    print("[Directory rename]\t@@ Looking for directories to rename...")
    for target_directory in search_directories:
        if target_directory.name.lower() == f"{REPLACEMENT_BASE}_NAME".lower():
            print(
                f"[Directory rename]\t\tRenaming '{target_directory}' to '{target_directory.parent / NEW_PROJECT_NAME}'"
            )
            if LIVE_MODE:
                target_directory.rename(target_directory.parent / NEW_PROJECT_NAME)
            success_count += 1

    if success_count <= 0:
        print("[Directory rename]\t@@ No directories renamed.")
    else:
        print(
            f"[Directory rename]\t@@ {success_count} directory{'s' if success_count > 1 else ''} renamed."
        )


if __name__ == "__main__":
    replacement_map = load_replacement_values()
    replace_placeholders(replacement_map)
    print("[Done]")
