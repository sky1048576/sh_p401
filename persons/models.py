from __future__ import unicode_literals

from django.db import models





from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    national_code = models.CharField(max_length=10)

class Home(models.Model):
    name = models.CharField(max_length=30,unique=True)
    ostan = models.CharField(max_length=2,default='0')
    shahrestan = models.CharField(max_length=120,default='0')
    address = models.TextField(default='abc')
    about = models.TextField(default='abc')
    zip_code = models.CharField(max_length=10,default='123')
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    member = models.ForeignKey(User)


    def __str__(self):
    	return str((self.pk))
    def get_absolute_url(self):
        return "/persons/home/%s/" %self.pk
class Picture(models.Model):
    homeid = models.ForeignKey(Home)
    image = models.ImageField(upload_to='persons')
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self):
        return (str(self.pk))
    # def get_absolute_url(self):
    #     return reverse("persons:detail_home", kwargs={"id": self.homeid})
    def get_absolute_url(self):
        return "/persons/home/%s/" %self.homeid

