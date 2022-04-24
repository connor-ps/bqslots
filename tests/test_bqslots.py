#!/usr/bin/env python

"""Tests for `bqslots` package."""

import pytest
import bqslots.client as bqs
import pathlib
import json
import shutil


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_write_dict_to_json_file(self):
    """
    test writing dict to file with path that does not exist
    :return:
    """
    test_data = {"dummy": 1}

    cwd_path = pathlib.Path().absolute().cwd()
    expected_path = str(cwd_path) + "/some/directory"

    expected_file_path = f"{expected_path}/output.json"
    bqs.Client.write_dict_to_json_file(expected_path, "output.json", test_data)

    actual_path = pathlib.Path(expected_file_path)
    self.assertTrue(actual_path.is_file())
    actual_data = json.loads(actual_path.read_text())
    self.assertEqual(test_data, actual_data)

    # clean up file and path
    shutil.rmtree(expected_path)