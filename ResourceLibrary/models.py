from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# from django.contrib.auth import get_user_model

# SUBJECTS = (
#     (0,"Maths"),
#     (1,"Physics"),
#     (2,"Global Perspectives"),
#     (3, "Computer Science")

# )
RESTYPE = (
    (0,"Detailed Notes"),
    (1,"Tools"),
    (2,"Revision Notes"),
    (3,"Endorsed Educationists"),
    (4, "Conceptual Resources")
)

class Subject(models.Model):
    name = models.CharField(max_length =20)
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length =20)
    def __str__(self):
        return self.name

class Entry(models.Model):
    name = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.SET("Deleted User"),related_name='resource_entries')
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    restype = models.IntegerField(choices=RESTYPE, default=0)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    level = models.ForeignKey(Level, on_delete=models.PROTECT)

    resourcelink = models.URLField(("ResourceURLs"), max_length=500, null=True,blank=True)
    embedlink = models.URLField(("VideoURLs"), max_length=500, null=True, blank=True)
    affiliateflag = models.BooleanField(("Paid Promotion"),default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    entry = models.ForeignKey(Entry,on_delete=models.CASCADE,related_name='comments')
    name = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


