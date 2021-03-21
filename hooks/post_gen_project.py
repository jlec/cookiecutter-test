#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_FOLDERS = (
    "hooks",
    "tests",
)


def create_folder(filepath):
    dir = os.path.join(PROJECT_DIRECTORY, filepath)
    if not os.path.isdir(dir):
        os.mkdir(dir)


def remove_file_or_folder(filepath):
    fp = os.path.join(PROJECT_DIRECTORY, filepath)
    if os.path.isdir(fp):
        shutil.rmtree(fp)
    else:
        os.remove(fp)


def gen_role_folders():
    for d in PROJECT_FOLDERS:
        create_folder(d)

def gen_template_folder():
    {%raw-%}
    shutil.move('cookiecutter.github_repo', "{{ cookiecutter.github_repo }}")
    {%endraw%}

if __name__ == "__main__":
    gen_role_folders()
    gen_template_folder()
