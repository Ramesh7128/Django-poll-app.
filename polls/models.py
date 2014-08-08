from django.db import models
import datetime

class Poll(models.Model):
	def __unicode__(self):
		return self.questions
	
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	was_published_today.short_description = 'published today?'

	questions = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	def __unicode__(self):
		return self.choice

	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()


# Create your models here.