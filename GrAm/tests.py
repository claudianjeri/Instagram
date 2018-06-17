from django.test import TestCase
from .models import Image, Profile, Comment
# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.claudia=Profile(bio="me and him", user=self.vicky)

class ImageTestClass(TestCase):
    def setUp(self):
        self.house=Image(caption="my dream", likes=20, profile=self.claudia)

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment=Comment(comments="this looks amazing", user=self.Claudia, image=self.house)

