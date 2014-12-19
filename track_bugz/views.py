from django.shortcuts import render

from django.http import HttpResponse


def test_view(request):
    return HttpResponse("TODO, use admin interface.", content_type="text/plain")
