from django.contrib import admin
from project_viewer.models import ProjectImage, Project, Skill

class ProjectImageInline(admin.StackedInline):
	model = ProjectImage
	extra = 2

class ProjectAdmin(admin.ModelAdmin):
	inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
