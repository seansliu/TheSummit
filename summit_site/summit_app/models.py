from django.db import models
from django.contrib.auth.models import User
#from djangotoolbox.fields import ListField


#---------------
# Summit Models |
#---------------


class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    #each question relates to one user in the auth_user collection
    user_id = models.ForeignKey(User)
    occupation = models.CharField(max_length=64)

    def __unicode__(self):
        return self.question_text
