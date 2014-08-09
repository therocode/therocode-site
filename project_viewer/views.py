from django.shortcuts import render
from django.views import generic

from project_viewer.models import Project

class IndexView(generic.ListView):
	template_name = 'pv/project_list.html'
	context_object_name = 'project_list'

	def get_queryset(self):
		"""
		List all projects
		"""
		return Project.objects.all()
