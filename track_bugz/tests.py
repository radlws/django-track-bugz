import json
import os
import uuid

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase


#TODO: Try TDD here first , mock objects

# TODO add factory boy?
#import factory # factory boy

# TODO: create a factory object with all the fields
# Can be used in TestCase like so:
# pending_nomination = NominationFactory.create(status=Nomination.STATUS.pending)
# has all fields of the model, but also populates fields with defaults as show below

# class NominationFactory(factory.DjangoModelFactory):
#     FACTORY_FOR = Nomination
#
#     slug = factory.Sequence(lambda n: 'slug-%d' % n)
#     community_name = 'community'
#     community_address = '1200 Batman St.'
#     community_city = 'Toronto'
#     community_province = 'ON'
#     community_postal_code = 'M4W 3R8'
#
#     question1 = '1' * 250
#     question2 = '2' * 250
#     question3 = '3' * 250
#     question4 = '4' * 250
#     question5 = '5' * 250
#
#     image1 = settings.MEDIA_URL + 'nominations/test.jpg'
#     image_release = True
#
#     title = 'mr'
#     first_name = 'Bruce'
#     last_name = 'Wayne'
#     email = 'therealbatman@example.com'
#     phone_number = '123-456-7890'
#     age = 35
#     agree_rules = True

# TODO: Test out the model, ie. make sure slug returns unique

# class NominationModelTests(TestCase):
#
#     def test_valid_slug_returns_unique_slug(self):
#         slug = Nomination.objects.get_valid_slug('test name')
#         self.assertEqual(slug, 'test-name')
#
#         for slug in ['test-name', 'test-name-1', 'test-name-2']:
#             NominationFactory.create(community_name='test name', slug=slug)
#
#         slug = Nomination.objects.get_valid_slug('test name')
#         self.assertEqual(slug, 'test-name-3')

# TODO: Test page loads, NominationPageLoadTests, list tests ??

# factory can us ecreate, and create batch !! )
# class NominationListTests(TestCase):
#
#     def test_page_loads(self):
#         # create a factory of timeline
#         TimelineFactory.create_with_phases(['nominations'], active='nominations')
#         # create a factory of nomination
#         pending_nomination = NominationFactory.create(status=Nomination.STATUS.pending)
#         # parent verificatoin nomination
#         parent_nomination = NominationFactory.create(status=Nomination.STATUS.parent_verification)
#         # all differen times of nominations creaed ...
#         image_review_nomination = NominationFactory.create(status=Nomination.STATUS.pending_image_review)
#         rejected_nomination = NominationFactory.create(status=Nomination.STATUS.rejected)
#         finalist_nomination = NominationFactory.create(status=Nomination.STATUS.finalist)
#         approved_nominations = NominationFactory.create_batch(3, status=Nomination.STATUS.approved)
#
#         # reverse view nominations list to view them all and get 200 response
#         response = self.client.get(reverse('nominations-list'))
#         self.assertEqual(response.status_code, 200)
#         # make sure right template is used
#         self.assertTemplateUsed(response, 'nominations/list.html')
#         #make sure response object has a nominations
#         self.assertIn('nominations', response.context)
#
#         # make sure that the right nominations are present in the nomination context  ie. approved hould be
#         # pending, parent, image review, rejected should not be
#         for nomination in [pending_nomination, parent_nomination, image_review_nomination, rejected_nomination]:
#             self.assertNotIn(nomination, response.context['nominations'])
#
#         for nomination in approved_nominations:
#             self.assertIn(nomination, response.context['nominations'])
#
#         self.assertIn(finalist_nomination, response.context['nominations'])
#
#     # test the finalist page
#     def test_finalists_page_loads(self):
#         # create a time factory wth phase finalists and make it active.
#         TimelineFactory.create_with_phases(['finalists'], active='finalists')
#         # create all nomination types + a list of nominations batch for finalists
#         pending_nomination = NominationFactory.create(status=Nomination.STATUS.pending)
#         parent_nomination = NominationFactory.create(status=Nomination.STATUS.parent_verification)
#         image_review_nomination = NominationFactory.create(status=Nomination.STATUS.pending_image_review)
#         rejected_nomination = NominationFactory.create(status=Nomination.STATUS.rejected)
#         approved_nomination = NominationFactory.create(status=Nomination.STATUS.approved)
#         finalist_nominations = NominationFactory.create_batch(3, status=Nomination.STATUS.finalist)
#
#         # show finalists list view store in response, check code is 200 on the page
#         response = self.client.get(reverse('nominations-finalists_list'))
#         self.assertEqual(response.status_code, 200)
#         # check template used
#         self.assertTemplateUsed(response, 'nominations/list.html')
#         # chck that nominations in context
#         self.assertIn('nominations', response.context)
#
#         # check correct nominations respond
#         for nomination in [approved_nomination, pending_nomination, parent_nomination, image_review_nomination, rejected_nomination]:
#             self.assertNotIn(nomination, response.context['nominations'])
#
#         for nomination in finalist_nominations:
#             self.assertIn(nomination, response.context['nominations'])



# FILTER Search via filters:

# need a dispatch to go to right action on method

#  need to see how queryset gets passed to it
# class NominationSearchFilter(filters.SearchFilter):
#
#     def filter_queryset(self, request, queryset, view):
#
#         # provinces
#         province = request.QUERY_PARAMS.get('community_province', None)
#         if province is not None:
#             queryset = queryset.filter(community_province=province)
#
#         # video
#         has_video = request.QUERY_PARAMS.get('has_video', None)
#         if has_video is not None:
#             queryset = queryset.filter(video_url__isnull=False)
#
#         # finalists
#         finalists_only = request.QUERY_PARAMS.get('show', '').lower() == 'finalists'
#         if finalists_only:
#             queryset = queryset.filter(status=Nomination.STATUS.finalist)
#
#         # search
#         search_fields = getattr(view, 'search_fields', None)
#         search_phrase = request.QUERY_PARAMS.get(self.search_param, '').strip()
#
#         if not search_phrase or not search_fields:
#             return queryset
#
#         orm_lookups = [self.construct_search(str(search_field))
#                        for search_field in search_fields]
#
#         or_queries = []
#         for search_term in self.get_search_terms(request):
#             or_queries.extend([Q(**{orm_lookup: search_term})
#                           for orm_lookup in orm_lookups])
#
#         province = PROVINCES_NORMALIZED.get(search_phrase.lower())
#         if province is not None:
#             or_queries.append(Q(community_province=province))
#
#         if not or_queries:
#             return queryset
#
#         return queryset.filter(reduce(operator.or_, or_queries))