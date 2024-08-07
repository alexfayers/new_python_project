"""Yoinked from https://github.com/zillionare/python-project-wizard/blob/2d85c2c267f98e68288c3716d4e92c815e4cba33/hooks/pre_gen_project.py."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.__project_slug}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        f"ERROR: The project slug ({module_name}) is not a valid Python module name. "
        "Please do not use a - and use _ instead"
    )

    # Exit to cancel project
    sys.exit(1)
