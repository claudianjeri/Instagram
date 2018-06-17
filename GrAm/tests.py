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
        #set up user class
        self.new_user = User(username="clau",email="clau@mail.com")
        self.new_user.save()
        #set up for profile class
        self.new_profile=Profile(bio="me and him",user=self.new_user)
        self.new_profile.save()
        #set up for Image class
        self.house=Image(caption="my dream house",likes=30,profile=self.new_profile)
        self.house.save_image()

    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.house,Image))

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.house.save_image()
        self.house.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)<1)

    def test_get_images(self):
        self.house.save_image()
        images = Image.get_images()
        self.assertEqual(len(images),1)

    def test_get_image_by_id(self):
        pass

class CommentTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user = User(username="clau",email="clau@mail.com")
        self.new_user.save()
        #set up for profile class
        self.new_profile=Profile(bio="me and him",user=self.new_user)
        self.new_profile.save()
        #set up for Image class
        self.house=Image(caption="my dream house",likes=30,profile=self.new_profile)
        self.house.save()
        #set up for comment class
        self.new_comment=Comment(comments="This is amazing",user=self.new_user,image=self.house)
        self.new_comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))

    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)

    def test_delete_comment(self):
        self.new_comment.save_comment()
        self.new_comment.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)<1)

    def test_get_comment(self):
        self.new_comment.save_comment()
        comment = Comment.get_comment()
        self.assertEqual(len(comment),1)
