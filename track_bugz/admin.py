from django.contrib import admin

# Register your models here.
from .models import Project, Ticket


# add filter by
# admin - can manage projects

# staff - create groups w/ diff access

#ticket actions
# resolve, set milestone, re-open, close,


# API : TODO

admin.site.register(Project)
admin.site.register(Ticket)