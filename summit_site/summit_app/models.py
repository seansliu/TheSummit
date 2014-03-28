import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
#from djangotoolbox.fields import ListField


#---------------
# Summit Models |
#---------------


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0)
    occupation = models.CharField(max_length=64)
    identity = models.CharField(max_length=64)

    def __str__(self):
        return "%s's profile" % self.user


class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, default=0)
    rating = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now()\
            - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __unicode__(self):
        return self.question_text


class Comment(models.Model):
    comment_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User)
    parent_question = models.ForeignKey(Question)
    parent_comment = models.ForeignKey('self', blank=True, null=True)
    COMMENT_TYPES = (
        ('Q', 'Question'),
        ('C', 'Comment'),
        ('L', 'Link'),
    )
    comment_type = models.CharField(max_length=1, choices=COMMENT_TYPES)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.comment_text
