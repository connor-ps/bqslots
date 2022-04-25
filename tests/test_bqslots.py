#!/usr/bin/env python

"""Tests for `bqslots` package."""

import unittest
import bqslots.slots_allocation as bqs
import pathlib
import json
import shutil


class TestBqSlots(unittest.TestCase):

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
