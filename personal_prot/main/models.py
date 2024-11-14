from django.db import models

# Create your models here.
class Main(models.Model):
    titel = models.CharField(max_length=2048)
    short_reviwe= models.CharField(max_length=2048)
    email = models.EmailField()
    about = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="https://images.pexels.com/photos/886521/pexels-photo-886521.jpeg")
    poster2 = models.ImageField(upload_to="images/", default=None)
    poster3 = models.ImageField(upload_to="images/", default=None)
    poster4 = models.ImageField(upload_to="images/", default=None)
    poster5 = models.ImageField(upload_to="images/", default=None)
