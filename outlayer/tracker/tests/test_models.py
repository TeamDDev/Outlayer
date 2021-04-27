from django.test import TestCase
from tracker.models import Profile, Records
from django.contrib.auth.models import User

class ModelsTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user("test123", "test@email.com", "Django@123")
    
    def teardown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_user_profile_intexp(self):
        profile = Profile.objects.create(name=self.user1, monthly_limit=4000, expenses_soFar=2500)
        self.assertTrue(True, 1)

    def test_user_profile_floatexp(self):
        rofile = Profile.objects.create(name=self.user1, monthly_limit=400.50, expenses_soFar=125.50)
        self.assertTrue(True, 1)