from django.test import TestCase
from django.contrib.auth.models import User
from bootcamp.activities.models import Activity
# Create your tests here.

class ActivityTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="user1", password="password")
        user = User.objects.get(username="user1")

        self.activity = Activity(user=user, activity_type='F')

    def tearDown(self):
        for activity in Activity.objects.all():
            activity.delete()

        for user in User.objects.all():
            user.delete()

    def testSaveNewActivity(self):
        self.activity.save();
        self.assertEqual(Activity.objects.all()[0], self.activity)
