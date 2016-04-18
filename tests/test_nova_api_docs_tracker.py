#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_nova_api_docs_tracker
----------------------------------

Tests for `nova_api_docs_tracker` module.
"""

import unittest

from nova_api_docs_tracker import main


class TestNova_api_docs_tracker(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_check_files(self):
        path = 'test_files'
        inc_files = main.get_inc_files(path)
        expected_names = ["test_files/flavors.inc", "test_files/images.inc", "test_files/servers.inc"]
        got_names = inc_files.keys()
        self.assertEquals(expected_names, got_names, "Check that filenames list is correct")

    def test_split_file(self):
        f = open("test_files/servers.inc", 'r')
        contents = f.read()
        got = main.split_inc_file(contents)
        expected_len = 11
        self.assertEquals(expected_len, len(got), "Check that file split is correct")

    def test_extract_stuff(self):
        f = open("test_files/servers.inc", 'r')
        contents = f.read()
        split_contents = main.split_inc_file(contents)
        got = main.extract_stuff(split_contents)
        expected_keys = ['body', 'methods']
        expected_methods = sorted(['Delete Server', 'List Servers', 'Show Server Details', 'Update Server'])
        self.assertEquals(expected_keys, got.keys(), "Check content keys")
        self.assertEquals(expected_methods, sorted(got['methods'].keys()), "check method keys")

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
