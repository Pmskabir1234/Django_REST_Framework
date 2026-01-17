from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField(max_length=500)

    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    comment = models.TextField(max_length=200, )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    # make sure u use related_names, this is will help in implementing 
    # nested serializers

    def __str__(self):
        return self.comment 