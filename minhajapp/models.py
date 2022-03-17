from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profilePic = models.ImageField(upload_to='images',default='images/default.jpg')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)
    def __str__(self) :
        return self.user.username



class Packages(models.Model):
    title = models.CharField(max_length=300)
    disc = models.TextField()
    thmbnail = models.ImageField(upload_to='thumbnail',null=False)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.slug


class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Cancel','Cancel'),
        ('Booked','Booked')
    )
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    customer = models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Packages,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    quan = models.IntegerField()
    
    
    