import datetime
from django.utils import timezone
from django.db import models

class Skill(models.Model):
	name = models.CharField(max_length = 200)
	skill_level = models.IntegerField()

	def __unicode__(self):
		return self.name

class Project(models.Model):
	title         = models.CharField(max_length = 200)
	creation_date = models.DateTimeField('date created')
	finish_date   = models.DateTimeField('date finished', blank=True, null=True)
	description   = models.CharField(max_length = 200)
	skills        = models.ManyToManyField(Skill)
	site          = models.URLField(blank=True, null=True)
	source        = models.URLField(blank=True, null=True)
	demo          = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return self.title

class ProjectImage(models.Model):
	image_text = models.CharField(max_length = 200)
	image      = models.ImageField("Image", upload_to="images/")
	project    = models.ForeignKey(Project)
