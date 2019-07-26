from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'photos/')
    bio = models.CharField(max_length =200)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    Img_name = models.CharField(max_length =30)
    Img_caption = models.CharField(max_length =100)
    Likes = models.IntegerField()
    Comments = models.CharField(max_length =200)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.Img_name

    def save_Img(self):
        self.save()
    
    
