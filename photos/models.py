from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'photos/')
    bio = models.CharField(max_length =200)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    @classmethod
    def user_has_profile(cls, user_id):
        profiles = Profile.objects.filter(user_id=user_id)
        return len(profiles) > 0

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    Img_name = models.CharField(max_length =30)
    Img_caption = models.CharField(max_length =100)
    Likes = models.IntegerField()
    profile = models.ForeignKey(Profile)
    comments = models.ForeignKey

    def __str__(self):
        return self.Img_name

    def save_Img(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_imagename(cls,search_term):
        photos = cls.objects.filter(Img_name__icontains=search_term)
        return photos

class Comment(models.Model):
    comment = models.CharField(max_length = 200)
    image = models.ForeignKey(Image)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()


    

    
