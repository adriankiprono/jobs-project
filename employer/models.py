from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Applicant(models.Model):
    
    first_name = models.CharField(max_length =30,null=True)
    last_name = models.CharField(max_length =30,null=True)
    email = models.EmailField()
    APPLICANT_CHOICES=(
        ('EMPLOYER','employer'),
        ('EMPLOYEE','employee'),
    )
    applicants=models.CharField(
        max_length=20,
        choices=APPLICANT_CHOICES,
    )
    job=models.CharField(max_length=50,null=True)
    descriptions=models.TextField(max_length=200,null=True)
    pay=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    picture = models.ImageField(upload_to='avatar/', default='default.jpg')
    post = HTMLField(null=True)

    @classmethod
    def search_by_job(cls,search_term):
        applicants = cls.objects.filter(job__icontains=search_term)
        return applicants

class User(models.Model):
    user_name=models.CharField(max_length=50,null=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='profile')
    profile_pic = models.ImageField(upload_to='image/', default='default.png')


    

