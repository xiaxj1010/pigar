# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import unittest
import os

from ..pypi import _extract_pkg_names


class ExtractHtmlTest(unittest.TestCase):

    def test_extract_names(self):
        path = os.path.join(os.path.dirname(__file__),
                            './fake_simple_html.txt')
        names = []
        with open(path) as f:
            _extract_pkg_names(f.read(), names.append)
        self.assertListEqual(names, 'a b c d e f g'.split())
