from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Branch, Event, Student, Blog, AvailableFeatures


# Register your models here.
# Student Admin Adding Filter Properties
class StudentAdmin(admin.ModelAdmin):
    list_display = ('event', 'student_name', 'email_id', 'mobile_number', 'roll_no', 'branch')
    search_fields = ('event__event_name', 'student_name', 'event__event_code', 'branch__branch_name')
    filter_horizontal = ()
    ordering = ()
    list_filter = ['event', 'branch', 'event__event_code']
    fieldsets = ()
    model = Student


# Event Admin Adding Filter Properties
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_code', 'current_status', 'pub_date')
    search_fields = ('event_name', 'event_code')
    filter_horizontal = ()
    ordering = ()
    list_filter = ['event_name', 'event_code']
    fieldsets = ()
    model = Event


class BlogAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'roll_no', 'subject')
    search_fields = ('student_name', 'roll_no')
    filter_horizontal = ()
    ordering = ()
    list_filter = ()
    fieldsets = ()
    model = Blog
    readonly_fields = ['student_name', 'roll_no', 'subject', 'suggestion']


class AvailableFeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature_name', 'current_status')
    search_fields = ('feature_name', 'current_status')
    filter_horizontal = ()
    ordering = ()
    list_filter = ['feature_name', 'current_status']
    fieldsets = ()
    model = AvailableFeatures
    readonly_fields = ['feature_name']

# Register The Models


admin.site.register(Branch)
admin.site.register(Event, EventAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(AvailableFeatures, AvailableFeaturesAdmin)
