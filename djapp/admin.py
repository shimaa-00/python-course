from django.contrib import admin

# Register your models here.
from .models import Student, Track


class CustomStudent(admin.ModelAdmin):
    fieldsets = (['student info', {
        'fields': ['fname', 'lname', 'age']
    }], ['track info', {
        "fields": ['student_track']
    }])
    list_display = ('fname', 'lname', 'age', 'student_track', 'is_adult')
    search_fields = ('fname', 'lname', 'age', 'student_track__track_name')
    list_filter = ('age', "student_track")


class InlineStudent(admin.StackedInline):
    model = Student
    extra = 1


class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]
    list_display = [('track_name')]


admin.site.register(Student, CustomStudent)
admin.site.register(Track, CustomTrack)
