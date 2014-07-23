import datetime
from django.utils import timezone
from django.db import models

class Project(models.Model):
	title = models.CharField(max_length = 200)
	creation_date = models.DateTimeField('date created')
	finish_date = models.DateTimeField('date finished', blank=True)
	description = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.title

class ProjectImage(models.Model):
	image_text = models.CharField(max_length = 200)
	image = models.ImageField("Image", upload_to="images/")
	project = models.ForeignKey(Project)
