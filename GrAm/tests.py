from django.test import TestCase
from .models import Image, Profile, Comment
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user = User(username="clau",email="clau@mail.com")
        self.new_user.save()
        #set up profile class
        self.claudia=Profile(bio="me and him", user=self.claudia)
        self.claudia.save_profile()

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.claudia,Profile))

    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_profile(self):
        self.claudia.save_profile()
        self.claudia.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)<1)

    def test_find_profile(self):
        self.claudia.save_profile()
        me = Profile.objects.all()
        profiles = Profile.find_profile('clau')
        self.assertEqual(profiles,profiles)

    def test_get_profile(self):
        self.claudia.save_profile()
        prof = Profile.get_profile()
        self.assertEqual(len(prof),1)

        
class ImageTestClass(TestCase):
    def setUp(self):
        self.house=Image(caption="my dream", likes=20, profile=self.claudia)

class CommentTestClass(TestCase):
    def setUp(self):
        self.comment=Comment(comments="this looks amazing", user=self.Claudia, image=self.house)

