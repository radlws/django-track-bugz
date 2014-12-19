from django.contrib import admin

# Register your models here.
from .models import Project, Ticket


# add filter by

admin.site.register(Project)
admin.site.register(Ticket)