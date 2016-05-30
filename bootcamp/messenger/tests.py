from django.test import TestCase
from bootcamp.messenger.models import Message
from django.contrib.auth.models import User


class MessageTest(TestCase):

    def setUp(self):
        User.objects.create(username="user1", password="password1")
        User.objects.create(username="user2", password="password2")
        self.sender_user = User.objects.get(username="user1")
        self.reciever_user = User.objects.get(username="user2")
        self.congratulations = "Hello. How are you?"
        Message.objects.create(
            from_user=self.sender_user,
            message=self.congratulations,
            user=self.sender_user,
            conversation=self.reciever_user,
            is_read=True)
        self.message_sent1 = Message.objects.get(message=self.congratulations)

    def test_send_message(self):
        self.assertTrue(self.congratulations, self.message_sent1.message)

    def test_send_message(self):
        self.assertTrue(self.sender_user, self.message_sent1.from_user)

    def test_send_message(self):
        message1 = Message()
        current_user_message = message1.send_message(
            self.sender_user, self.reciever_user, self.congratulations)
        self.assertEquals(current_user_message.from_user, self.sender_user)
        self.assertEquals(current_user_message.user, self.reciever_user)
        self.assertItemsEqual(
            current_user_message.message, self.congratulations)

    """def test_get_conversations(self):
        good_morning = "Good morning!"
        Message.objects.create(
            from_user=self.sender_user,
            message=good_morning,
            user=self.sender_user,
            conversation=self.reciever_user,
            is_read=False)
        message_sent2 = Message.objects.get(message=good_morning)
        users = []
        users.append({'user': message_sent2.user.id, 'last':message_sent2.message, 'unread':0 })
        self.assertEqual(users, message_sent2.get_conversations(self.reciever_user))
        """
