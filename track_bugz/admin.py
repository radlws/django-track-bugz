from django.contrib import admin


#from django.utils.translation import ugettext_lazy as _   # TODO: add translation
#from django.contrib import messages


# Register your models here.
from .models import Project, Ticket, Milestone


# add filter by
# admin - can manage projects

# staff - create groups w/ diff access

#ticket actions
# resolve, set milestone, re-open, close,


# API : TODO


# TODO: How to display sub tickets in admin ?

class TicketAdmin(admin.ModelAdmin):
    #form = ProjectForm
    model = Ticket
    list_display = ('project', 'milestone', 'title', 'opened_by', 'assigned_to', 'status')
    search_fields = ('title', )
    list_filter = ('project', 'status', ) # TODO
    #prepopulated_fields = {"slug": ("name",)}  # TODO: later


    #actions = ['update_project_from_api', 'reset_project_api_values']


# TODO: Will need get_formsets

# For example if you wanted to display a particular inline only in the change view, you could override get_formsets as follows:
#
# class MyModelAdmin(admin.ModelAdmin):
#     inlines = [MyInline, SomeOtherInline]
#
#     def get_formsets(self, request, obj=None):
#         for inline in self.get_inline_instances(request, obj):
#             # hide MyInline in the add view
#             if isinstance(inline, MyInline) and obj is None:
#                 continue
#             yield inline.get_formset(request, obj)
#

# more her: https://docs.djangoproject.com/en/1.7/ref/contrib/admin/

admin.site.register(Ticket, TicketAdmin)

admin.site.register(Milestone)


class MilestoneInlineAdmin(admin.TabularInline):
    model = Milestone
    extra = 0
    #readonly_fields = ['name', 'bedrooms', 'bathrooms', 'sqft', ]
    #exclude = ['no_bedrooms', 'no_bathrooms', 'model_id']

    can_delete = True
    # #max_num = ?  #TODO: establish the max & add to homepage as well

    # TODO: Permissions based on project_team in project to come later
    #def has_add_permission(self, request):
    #    return False

# class SAMPPLE(admin.TabularInline):
#     model = FloorPlan
#     extra = 0
#     readonly_fields = ['name', 'bedrooms', 'bathrooms', 'sqft', ]
#     exclude = ['no_bedrooms', 'no_bathrooms', 'model_id']
#     # model = ProjectSlide
#     # extra = 0
#     # can_delete = True
#     # #max_num = ?  #TODO: establish the max & add to homepage as well
#
#     def has_add_permission(self, request):
#         return False


class ProjectAdmin(admin.ModelAdmin):
    #form = ProjectForm
    model = Project
    list_display = ('name', 'creation_date', 'modified_date')
    search_fields = ('name', )
    #list_filter = ('active', ) # TODO
    #prepopulated_fields = {"slug": ("name",)}  # TODO: later

    inlines = (MilestoneInlineAdmin, )

    #actions = ['update_project_from_api', 'reset_project_api_values']




# class MilestoneAdmin(admin.ModelAdmin):
#
#     fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('name',)}
#         ),
#         (_('General Info'), {'fields': ('email', 'tile_image', 'description', )}),
#         (_('Estimates'), {'fields': ('suite_min_price', 'suite_max_price', 'suite_min_sqft', 'suite_max_sqft', 'estimated_occupancy_date', 'vip_launch_date',
#                                      'estimated_maintenance', )}),
#         (_('API & Site Options'), {'fields': ('phase_id', 'slug', 'active', ),
#                                    'description': '<div class="help">Price & SqFt used only if model data is not available.</div>'}),
#         (_('API Info'), {'fields': ('address', 'city', 'province', 'country', 'latitude', 'longitude',
#                                     'postal_code', 'website', 'main_intersection', 'development_type', 'builders'),
#                          'description': '<div class="help">This content is updated daily from the API</div>'}),
#     )
#
#


admin.site.register(Project, ProjectAdmin)