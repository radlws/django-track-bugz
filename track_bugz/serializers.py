from django.core.serializers.json import DjangoJSONEncoder
from django import http
import json
from django.db.models import F
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import get_object_or_404


class JSONResponse(http.HttpResponse):
    def __init__(self, response, *args, **kwargs):
        json_response = json.dumps(response)

        kwargs['content'] = json_response
        kwargs['mimetype'] = kwargs.get('mimetype', 'application/json')

        super(JSONResponse, self).__init__(*args, **kwargs)


# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)

# import json
#
# from django import http
#
# from .serializers import JSONEncoder
#
#
# class JSONResponse(http.HttpResponse):
#
#     def __init__(self, context, **response_kwargs):
#         content = json.dumps(context, cls=JSONEncoder)
#
#         response_kwargs['content'] = content
#         response_kwargs['mimetype'] = 'application/json'
#
#         super(JSONResponse, self).__init__(**response_kwargs)
#
#         self['Cache-Control'] = 'no-cache'


def get_tickets(request, ticket_id=None, milestone_name=None, status=None, ticket_type=None):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    #poll = get_object_or_404(cc_models.Poll, id=poll_id)

    try:
        choice_id = int(request.POST.get('choice', None))
    except:
        return HttpResponseBadRequest

    #if user_voted(request, poll.id):
    #    return JSONResponse({'messages': ['already voted']}, status=400)

    #updated = cc_models.PollChoice.objects.filter(id=choice_id, poll_id=poll_id).update(votes=F('votes') + 1)

    # if updated:
    #     response = JSONResponse({
    #         'results': poll.to_dict()
    #     })
    #     update_votes(request, response, poll.id)
    #     return response

    return JSONResponse({'messages': ['error updating votes']}, status=400)

# from django.forms import widgets
# from rest_framework import serializers
# from .models import Milestone, Ticket
# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
#
#
# class TicketSerializer(serializers.HyperlinkedModelSerializer):
#     #owner = serializers.ReadOnlyField(source='owner.username')
#     #link_field = serializers.HyperlinkedIdentityField(view_name='linkout', format='html')
#
#     class Meta:
#         model = Ticket
#         # fields = ('url', 'highlight', 'owner',
#         #           'title', 'code', 'linenos', 'language', 'style')
#
#
# # class UserSerializer(serializers.HyperlinkedModelSerializer):
# #     #tickets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
# #
# #     class Meta:
# #         model = User
# #         fields = ('url', 'username', 'snippets')