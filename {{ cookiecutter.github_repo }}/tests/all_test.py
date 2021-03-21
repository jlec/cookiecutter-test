# -*- coding: utf-8 -*-
import datetime
import os
import shlex
import subprocess
import sys

import pytest

from contextlib import contextmanager

from cookiecutter.utils import rmtree

FILES = (
    ".gitignore",
    ".mdlrc",
    ".pre-commit-config.yaml",
    ".prettierignore",
    "LICENSE",
    "pyproject.toml",
    "README.md",
    "Taskfile.yml",
    "VERSION",
)

DIRS = (
    ".ci",
    "control",
)


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def check_project_content(result, files=(), dirs=()):
    assert result.exit_code == 0
    found_toplevel_files = [f.name for f in result.project_path.iterdir()]

    for f in files:
        assert result.project_path.joinpath(f).is_file()
        found_toplevel_files.remove(f)
    for d in dirs:
        assert result.project_path.joinpath(d).is_dir()
        found_toplevel_files.remove(d)
    try:
        assert len(found_toplevel_files) == 0
    except AssertionError as e:
        print(found_toplevel_files)
        raise e


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies"""
    project_path = str(result.project_path)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "Taskfile.yml" in found_toplevel_files
        assert "README.md" in found_toplevel_files


def test_make_help(cookies):
    with bake_in_temp_dir(cookies) as result:
        output = check_output_inside_dir("task --list", str(result.project_path))
        assert b"task: Available tasks for this project:" in output


def test_bake_invalid_name(cookies):
    bake_in_temp_dir(cookies, extra_context={"project_slug": "foo-bar"})


def test_bake(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.exit_code == 0
        check_project_content(result, FILES, DIRS)
