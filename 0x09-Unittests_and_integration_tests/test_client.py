#!/usr/bin/env python3
"""test module"""
from client import GithubOrgClient
from unittest.mock import patch, Mock
from unittest import mock
from parameterized import parameterized, parameterized_class
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """test class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, name, mock):
        """test org"""
        myVal = GithubOrgClient(name)
        myVal.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{name}')
