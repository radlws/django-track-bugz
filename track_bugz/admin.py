from django.contrib import admin


#from django.utils.translation import ugettext_lazy as _   # TODO: add translation
#from django.contrib import messages


# Register your models here.
from .models import Project, Ticket, Milestone, TicketItem


# add filter by
# admin - can manage projects

# staff - create groups w/ diff access

#ticket actions
# resolve, set milestone, re-open, close,


# API : TODO


# TODO: How to display sub tickets in admin ? no need for this now

class TicketItemInlineAdmin(admin.TabularInline):
    model = TicketItem
    extra = 0
    readonly_fields = ['created_date', ]
    exclude = ['user']

    can_delete = False

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            pass
        print obj
        print request
        #TODO: update user charfield on save

        super(TicketItemInlineAdmin, self).save_model(request, obj, form, change)


class TicketAdmin(admin.ModelAdmin):
    #form = TicketForm
    model = Ticket
    list_display = ('project', 'milestone', 'title', 'opened_by', 'assigned_to', 'status')
    search_fields = ('title', )
    list_filter = ('project', 'status', ) # TODO
    exclude = ('priority', )
    inlines = (TicketItemInlineAdmin, )
    #readonly_fields = ('opened_by', )
    #prepopulated_fields = {"slug": ("name",)}  # TODO: later

    actions = ['resolve_tickets', 'close_tickets', 'reopen_tickets', 'set_milestone']

    def resolve_tickets(self, request, queryset):
        pass
    resolve_tickets.short_description = "Resolve Tickets."

    def close_tickets(self, request, queryset):
        pass
    close_tickets.short_description = "close_tickets"

    def reopen_tickets(self, request, queryset):
        pass
    reopen_tickets.short_description = "reopen_tickets"

    def set_milestone(self, request, queryset):
        from django.shortcuts import render_to_response
        from django.template import RequestContext
        from django.http import HttpResponseRedirect
        from forms import MilestoneSelectForm
        form = MilestoneSelectForm(request.POST or None)

        set_project = None
        for obj in queryset:
            if not set_project:
                set_project = obj.project
            else:
                if obj.project != set_project:
                    self.message_user(request, 'Select only tickets for same project.')
                    return HttpResponseRedirect(request.get_full_path())

        if request.POST:
            self.message_user(request, 'Posted action!')
        # if 'cancel' in request.POST:
        #     self.message_user(request, 'Cancelled action.')
        #     return
        # elif 'link_series' in request.POST:
        #     form = self.SeriesForm(request.POST)
        #     if form.is_valid():
        #         series = form.cleaned_data['series']
        #         for x in queryset:
        #             y = Link(series=series, comic=x)
        #             y.save()
        #         self.message_user(request, self.categorySuccess.render({'count':queryset.count(), 'series':series}))
        #         return redirect(request.get_full_path())
        # if not form:
        #     form = self.SeriesForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        return render_to_response('select_milestone.html', {'q': queryset, 'form': form, 'path': request.get_full_path()},
                                  context_instance=RequestContext(request))
    set_milestone.short_description = "set_milestone"

    #permissions when set to closed

    # def has_add_permission(self, request, obj=None):
    #     if obj and obj.status == 'C':
    #         return False
    #
    # def has_change_permission(self, request, obj=None):
    #     if obj and obj.status == 'C':
    #         return False

    # def has_add_permission(self, request, obj=None):
    #     return False
    # def save_model(self, request, obj, form, change):
    #     #print obj.opened_by, 'done'
    #     #if not obj.opened_by:
    #     #print  dir(obj)
    #     #print obj.opened_by
    #     print obj.id
    #     obj.opened_by = request.user
    #     super(TicketAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('project', 'opened_by', )
        return self.readonly_fields


# TODO: if need to differ show inlines or not based on obj existence
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