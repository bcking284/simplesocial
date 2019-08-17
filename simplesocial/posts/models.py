from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse
from django.conf import settings
import misaka
from groups.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()
# connect current post to whoeber is logged into session

class Post(models.Model):
    # going to set up attributed for post
    # set up string representation for Post
    # save method
    # get_absolute_url method. Once someone has posted, where to send them
    user = models.ForeignKey(User,related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']
