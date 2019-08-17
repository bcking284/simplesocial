from django.db import models
from django.utils.text import slugify
#gets rid of chars that arent alphanumeric, underscore
import misaka
# link embedding, pip install
from django.contrib.auth import get_user_model
# allows me to call things off user's session
from django.core.urlresolvers import reverse

User = get_user_model()
from django import template
register = template.Library()
# will explain

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=256,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html= models.TextField(editable=False,default = '')
    members= models.ManyToManyField(User,through = 'GroupMember')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs = {'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group=models.ForeignKey(Group,related_name = 'memberships')
    # means that member is related to the group class
    user = models.ForeignKey(User, related_name='user_groups')
    #have user current that will have groups
    def __str__(self):
        return self.User.username
    class Meta:
        unique_together = ('group','user')
