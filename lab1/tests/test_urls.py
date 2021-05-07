from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, project

class TestUrls(SimpleTestCase):

    def test_home_is_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home.home)

    def test_create_project_is_resolved(self):
        url = reverse("project")
        self.assertEquals(resolve(url).func, project.create_project)

    def test_show_projects_is_resolved(self):
        url = reverse("show_projects")
        self.assertEquals(resolve(url).func, home.show_projects)

    def test_categories_is_resolved(self):
        url = reverse("categories")
        self.assertEquals(resolve(url).func, project.categories)     

    def test_project_details_is_resolved(self):
        url = reverse("project_details", args=[1])
        self.assertEquals(resolve(url).func, project.project_details)     

    