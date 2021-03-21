#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

ROLE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

project_slug = "{{ cookiecutter.cookiecutter_slug }}"

if not re.match(ROLE_REGEX, project_slug):
    print(f"ERROR: '{project_slug}' is not a valid Python module name!")

    # exits with status 1 to indicate failure
    sys.exit(1)
