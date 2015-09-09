import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # Used when printing objects as well as in Django admin
    # __str__ in Python 3
    def __unicode__(self):
    	return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # Specifies how to order or sort this field
    # By default, arbitrary methods can't be ordered
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    # Description of this field, used in Django admin
    was_published_recently.short_description = 'Published recently?'
    	


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
    	return self.choice_text