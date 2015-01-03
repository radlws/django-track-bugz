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