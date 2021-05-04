#!/usr/bin/python3
import unittest
import web_parser as wp

import requests

class WebParserTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = "https://www.naver.com/"
        cls.soup = wp.get_soup(url)

    def test_get_js_scripts(cls):
        res_js = wp.get_js_scripts(cls.soup)
        cls.assertNotEqual(res_js, None)
        print(res_js)

    def test_get_link_lists(cls):
        res_link = wp.get_links(cls.soup)
        cls.assertNotEqual(res_link, None)
        print(res_link)


if __name__=="__main__": 
    unittest.main()