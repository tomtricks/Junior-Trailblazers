from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# from tkinter import CASCADE
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # this is to send redirect to article page
        # return reverse('article-detail',args=(str(self.id)) ) 
        return reverse('home')



class Post(models.Model):
    title=models.CharField(max_length=255,blank=False)
    title_tag=models.CharField(max_length=255) #, default="GOOD BLOG" also can be used
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    #try
    college_name=models.CharField(max_length=255)
    event_date=models.DateTimeField(default=datetime.now)
    #tryy

    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    publication_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User,related_name='blog_post')
    
    register_url = models.CharField(max_length=255,null=True,blank=False,default='https://forms.gle/g8yyJ5LhJtJwz4Jy6')

    snippet = models.CharField(max_length=255)

    header_image = models.ImageField(null=True, blank=True, upload_to = "images/")



    def total_likes(self):
        return self.likes.count()

    
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # this is to send redirect to article page
        # return reverse('article-detail',args=(str(self.id)) ) 
        return reverse('home')
    
    @property
    def Days_till(self):
        today=date.today()
        days_till=self.event_date.date() - today
        days_till_stripped = str(days_till).split(",",1)[0]
        return days_till_stripped

    @property
    def Is_Past(self):
        today=date.today()
        if self.event_date.date() < today:
            thing="Past"
        else:
            thing="Furture"
        return thing


# TO edit user profile
class Profile(models.Model):
    user = models.OneToOneField(User, null=True ,on_delete=models.CASCADE)
    # bio = models.TextField()
    bio=RichTextField(blank=True,null=True)
    profile_pic = models.ImageField(null=True,blank=False, upload_to="images/profile/")
    website_url = models.CharField(max_length=255,null=True,blank=False)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)    
    instagram_url = models.CharField(max_length=255,null=True,blank=True)    
    twitter_url = models.CharField(max_length=255,null=True,blank=True)    


    def __str__(self):
        return str(self.user) 

    def get_absolute_url(self):
        # this is to send redirect to article page
        # return reverse('article-detail',args=(str(self.id)) ) 
        return reverse('home')