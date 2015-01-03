from django.conf.urls import patterns, include, url
#from views import TicketViewSet

# from rest_framework.routers import DefaultRouter
#
# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'tickets', TicketViewSet)
# #router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', 'track_bugz.views.test_view', name="default"),

]
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'track_bugz.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     # FOREIGNKEY & GENERIC LOOKUP
#     url(r'', 'track_bugz.views.test_view', name="default"),
#     #url(r'^lookup/related/$', RelatedLookup.as_view(), name="grp_related_lookup"),
#     #url(r'^lookup/m2m/$', M2MLookup.as_view(), name="grp_m2m_lookup"),
#     #url(r'^lookup/autocomplete/$', AutocompleteLookup.as_view(), name="grp_autocomplete_lookup"),
#     #url(r'^admin/', include(admin.site.urls)),
# )
