from http import HTTPStatus

from django.test import TestCase, override_settings
from django.test.client import Client


class IPBlacklistMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()

    @override_settings(BANNED_IPS=None)
    def test_request_successful_without_blacklist_setting(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @override_settings(BANNED_IPS=["192.168.1.2"])
    def test_request_successful_with_non_blacklisted_ip(self):
        response = self.client.get("/", REMOTE_ADDR="192.168.1.1")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @override_settings(BANNED_IPS=["192.168.1.2"])
    def test_request_fail_with_blacklisted_ip(self):
        response = self.client.get("/", REMOTE_ADDR="192.168.1.2")
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
