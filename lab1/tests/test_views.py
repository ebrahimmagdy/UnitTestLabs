from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, project
import json


class TestViews(TestCase):

    def test_home_GET(self):
        client=Client()
        response=client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_create_project_GET(self):
        client=Client()
        response=client.get(reverse("project"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "project/project_form.html")

    def test_project_details_GET(self):
        client=Client()
        response=client.get(reverse("project_details", args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "project/project_details.html")