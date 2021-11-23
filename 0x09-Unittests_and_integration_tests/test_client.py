#!/usr/bin/env python3
"""test module"""
from client import GithubOrgClient
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
import unittest
import requests
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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

    def test_public_repos_url(self):
        """test class"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @mock.patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """test class"""
        mock_get_json.return_value = [{"name": "google"},
                                      {"name": "abc"}]
        with mock.patch.object(GithubOrgClient, "_public_repos_url",
                               new_callable=PropertyMock) as mock_pb:
            mock_pb.return_value = "http://testurl.com"
            g_client = GithubOrgClient("facebook")
            result = g_client.public_repos()
            self.assertEqual(result, ["google", "abc"])
            mock_get_json.assert_called_once()
            mock_pb.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """test class"""
        git_client = GithubOrgClient("facebook")
        result = (git_client.has_license(repo, license))
        self.assertEqual(result, expected)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """test class"""
        def setUpClass(cls) -> None:
            """test class"""
            cls.get_patcher = patch('request.get', slide_effect=HTTPError)

            @classmethod
            def tearDownClass(cls):
                """test class"""
                cls.get_patcher.stop()

            def test_public_repos(self):
                """test class"""
                test_class = githubOrgClient("holberton")
                self.assertTrue()

            def test_public_repos_with_license(self):
                """test class"""
                test_class = GithubOrgClient("holberton")
                self.assertTrue()
