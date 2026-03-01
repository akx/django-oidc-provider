from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class CommandsTest(TestCase):
    def test_creatersakey_output(self):
        out = StringIO()
        call_command("creatersakey", stdout=out)
        assert "RSA key successfully created" in out.getvalue()

    def test_makemigrations_output(self):
        out = StringIO()
        call_command("makemigrations", "oidc_provider", stdout=out)
        assert "No changes detected in app" in out.getvalue()
