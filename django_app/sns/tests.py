# # リスト5-36 p.410
# from django.test import TestCase
# class SnsTests(TestCase):
#     def test_check(self):
#         x = True
#         self.assertTrue(x)
#         y = 100
#         self.assertGreater(y, 0)
#         arr = [10, 20, 30,]
#         self.assertIn(20, arr)
#         nn = None
#         self.assertIsNone(nn)

# # リスト5-37 p.412
# from django.test import TestCase
# class SnsTests(TestCase):
#     def test_check(self):
#         x = True
#         self.assertTrue(x)
#         y = 0
#         self.assertGreater(y, 100)
#         nn = None
#         self.assertIsNone(nn)

# # リスト5-39 p.416
# from django.test import TestCase

# from django.contrib.auth.models import User
# from .models import Message

# class SnsTests(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         usr = cls.create_user()
#         cls.create_message(usr)

#     @classmethod
#     def create_user(cls):
#         User(username = "test", password ="test", is_staff = True).save()
#         usr = User.objects.filter(username = "test").first()
#         return (usr)

#     @classmethod
#     def create_message(cls, usr):
#         Message(content = "this is test message", owner_id = usr.id).save()
#         Message(content = "test", owner_id = usr.id).save()
#         Message(content = "ok", owner_id = usr.id).save()
#         Message(content = "ng", owner_id = usr.id).save()
#         Message(content = "finish", owner_id = usr.id).save()

#     def test_check(self):
#         usr = User.objects.first()
#         self.assertIsNotNone(usr)
#         msg = Message.objects.first()
#         self.assertIsNotNone(msg)

# リスト5-40 p.417
from django.test import TestCase

from django.contrib.auth.models import User
from .models import Message

class SnsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        usr = cls.create_user()
        cls.create_message(usr)

    @classmethod
    def create_user(cls):
        User(username = "test", password ="test", is_staff = True).save()
        usr = User.objects.filter(username = "test").first()
        return (usr)

    @classmethod
    def create_message(cls, usr):
        Message(content = "this is test message", owner_id = usr.id).save()
        Message(content = "test", owner_id = usr.id).save()
        Message(content = "ok", owner_id = usr.id).save()
        Message(content = "ng", owner_id = usr.id).save()
        Message(content = "finish", owner_id = usr.id).save()

    def test_check(self):
        usr = User.objects.filter(username = "test").first()
        msg = Message.objects.filter(content = "test").first()
        self.assertIs(msg.owner_id, usr.id)
        self.assertEqual(msg.owner.username, usr.username)

        c = Message.objects.all().count()
        self.assertIs(c, 5)

        msgs = Message.objects.filter(content__contains = "test").all()
        self.assertIs(msgs.count(), 2)

        msg1 = Message.objects.all().first()
        msg2 = Message.objects.all().last()
        self.assertIsNot(msg1, msg2)
