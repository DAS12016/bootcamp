from django.test import TestCase
from django.contrib.auth.models import User
from bootcamp.activities.models import Activity, Notification
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


class NotificationTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="user1", password="password")
        User.objects.create(username="user2", password="password")
        user1 = User.objects.get(username="user1")
        user2 = User.objects.get(username="user2")

        self.notification = Notification(notification_type='L',
                                         from_user=user1, to_user=user2)
        self.notification.save()

    def tearDown(self):
        for user in User.objects.all():
            user.delete()

    def testGetSummary(self):
        self.assertEqual(Notification.objects.all()[0].get_summary("No post"), "No post")
