from django.test import TestCase
from .models import Profile,Image
# Create your tests here.

# Create your tests here.

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Biography= Profile(profile_photo = '/home/feven/Pictures/Moringa_pics', bio ='This is my biography')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Biography,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.Biography.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Biography= Profile(profile_photo = '/home/feven/Pictures/Moringa_pics', bio ='This is my biography')
        self.Biography.save_profile

        self.new_post= Image(image = '/home/feven/Pictures/Moringa_pics',Img_name = 'Haemathus',Img_caption = 'Its fouond in Africa', Likes = 4,  Comments = 'Its beautiful', profile  = self.Biography)
        self.new_post.save()

        self.new_post.Profile.add(self.profiles)


    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
   
