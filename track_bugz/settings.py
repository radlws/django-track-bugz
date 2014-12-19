# coding: utf-8

# reference proj
# https://github.com/sehmaschine/django-grappelli/tree/master/grappelli

# DJANGO IMPORTS
from django.conf import settings

# Settings
#_P = getattr(settings, "ADMIN_P", 'Default')


# Gets the layout style
#TODO:
# milestone - phase
# feature - user stories / epics
# etc .. WIP
TRACK_BUGZ_AGILE = getattr(settings, "TRACK_BUGZ_AGILE", False)

