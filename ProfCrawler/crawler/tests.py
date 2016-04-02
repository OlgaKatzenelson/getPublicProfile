from django.test import TestCase

from crawler import views

class ProfileMethodTests(TestCase):

    TEST_URL = "https://www.linkedin.com/in/olga-katzenelson-02b3a99"

    def test_get_existing_profile(self):
        """
        get_profile_html_by_url() should return a json object with [data]=profile if a profile exists
        or [error]='Profile does not exist' if not.
        """
        response = views.get_profile_html_by_url(self.TEST_URL)
        self.assertContains(response, "katzenelson")
        self.assertNotContains(response, "Profile does not exist")

    def test_get_not_existing_profile(self):
        """
        get_profile_html_by_url() should return a json object with [data]=profile if a profile exists
        or [error]='Profile does not exist' if not.
        """
        response = views.get_profile_html_by_url("https://www.linkedin.com/in/olga-katzenelson-02b3a9")
        self.assertContains(response, "Profile does not exist")
        self.assertNotContains(response, "katzenelson")

    def test_get_empty_url(self):
        """
        get_profile_html_by_url() should return a json object with [data]=profile if a profile exists
        or [error]='Profile does not exist' if not.
        """
        response = views.get_profile_html_by_url("")
        self.assertContains(response, "Please enter a valid url which starts with http")

    def test_get_number_of_top_skills_by_url(self):
        """
        get_number_of_top_skills_by_url() should return a json object with [data]=number_of_top_skills if a profile exists
        or [error]='Something went wrong. Try again.' if not.
        """

        views.get_profile_html_by_url(self.TEST_URL)
        response = views.get_number_of_top_skills_by_url(self.TEST_URL)
        self.assertContains(response, 17)